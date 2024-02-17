from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, current_user

views = Blueprint('views', __name__)

#create basic routes
@views.route('/')
def home():
    return render_template('todos.html')

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
           print('User already exists!')
        else:
            new_user = User(email=email, firstName=firstName, password=password1)
            db.session.add(new_user)
            db.session.commit()
            print('Account created!')
            # Once signed up log user in
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
     return render_template('signup.html')

@views.route('/login')
def login():
     # check user details and login
     return render_template('login.html')