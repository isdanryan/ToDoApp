from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#create basic routes
@views.route('/')
def home():
    return render_template('todos.html')

@views.route('/signup')
def signup():
     # register user details and add to database
     return render_template('signup.html')

@views.route('/login')
def login():
     # check user details and login
     return render_template('login.html')