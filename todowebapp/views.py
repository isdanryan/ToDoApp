from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json
from .models import User, Note
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)

#create basic routes
@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('todos.html', user=current_user)

# JS event calls route, retrives data and removes from database
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note successfully deleted!', category='success')
            return jsonify({})

# Sign Up page and function
@views.route('/signup', methods=['GET', 'POST'])
def signup():
     # Check to see if POST method is called and if TRUE store user inputs
     if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
     
        # Check to see if user already exists
        # If FALSE create user from above data and write to database
        user = User.query.filter_by(email=email).first()
        if user:
           # Pass message to flash handler for display on page.
           # Set category to control display style 'error' = red, 'success' = green
           flash('Email address already exists!', category='error')
        elif len(email) < 6:
            flash('Email must be greater than 6 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be greater than 8 characters.', category='error')
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
     return render_template("signup.html", user=current_user)

@views.route('/login', methods=['GET', 'POST'])
def login():
    # Check to see if POST method is used if so store user inputs
    if request.method == 'POST':
        email= request.form.get('email')
        password=request.form.get('password')
        
        # Check database for existing user
        user = User.query.filter_by(email=email).first()
        # If user exists check password match
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
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