from dotenv import load_dotenv
import os
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Load enviroment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# Establish database name and path
db = SQLAlchemy()
DB_NAME = "database.db"
DB_PATH = path.abspath("todowebapp\database.db")
directory = path.dirname(DB_PATH)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.abspath(DB_PATH)}'
    db.init_app(app)

    # Import routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # Import database structure from models.py
    from .models import User, Note
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    # Use flask login to check for and manage user sessions
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Check for and create database
def create_database(app):
    if not path.exists(DB_PATH):
        with app.app_context():
            db.create_all()
            print('Created database!')