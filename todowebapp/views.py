from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#create basic routes
@views.route('/')
def home():
    return render_template('todos.html')