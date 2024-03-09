from flask import (
    Blueprint, render_template, request, redirect,
    url_for, flash, jsonify, json
)
from .models import User, Note
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re

views = Blueprint('views', __name__)

# Route for the home page where users can view and add notes
@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            # Add a new note to the database for the current user
            new_note = Note(data=note, done=False, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    # Render the todos.html template with the current user's information
    return render_template('todos.html', user=current_user)

# Endpoint to handle requests to delete a note using json from js script
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note successfully deleted!', category='success')
            return jsonify({})


@views.route('/edit-note/<int:id>')
def edit_note(id):
    note_id = id
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            note.done = not note.done  # Toggle done on or off
            db.session.commit()
            return redirect(url_for('views.home'))

# Function to handle user sign up requests
@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        # Check if the email address already exists in the database
        # And check for password formatting
        if user:
            flash('Email address already exists!', category='error')
        elif len(email) < 6:
            flash('Email must be greater than 6 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters.', category='error')
        elif (regex.search(password1) == None):
            flash('Password must contain at leaset 1 special character.', category='error')
        elif not any(char.isdigit() for char in password1):
            flash('Password must contain at least 1 number.', category='error')
        else:
            new_user = User(
                email=email,
                firstName=first_name,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("signup.html", user=current_user)

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')      
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the password matches the hashed password stored
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                # Redirect the user to the home page after successful login
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist!', category='error')
    return render_template("login.html")


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.login'))
