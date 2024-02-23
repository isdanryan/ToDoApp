from dotenv import load_dotenv # Use dotenv to load enviroment variables
import os
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Load environment variables from .env file
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# Establish database name and path
db = SQLAlchemy()  # Initialize SQLAlchemy for database operations
DB_NAME = os.getenv("DATABASE_NAME") 
DB_PATH = path.abspath(os.getenv("DATABASE_PATH"))
directory = path.dirname(DB_PATH)  # Get the directory name of the database file

def create_app():
    app = Flask(__name__)  # Create Flask application instance
    app.config['SECRET_KEY'] = SECRET_KEY  # Set the secret key for the Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.abspath(DB_PATH)}'  # Set the database URI
    db.init_app(app)  # Initialize the database with the Flask app

    # Import routes
    from .views import views  # Import the views blueprint
    app.register_blueprint(views, url_prefix='/')  # Register the views blueprint with the app

    # Import database structure from models.py
    from .models import User, Note  # Import User and Note models
    create_database(app)  # Create the database if it doesn't exist

    login_manager = LoginManager()  # Create LoginManager instance
    login_manager.login_view = 'views.login'  # Set the login view for the LoginManager
    login_manager.init_app(app)  # Initialize LoginManager with the Flask app

    # Use flask_login to check for and manage user sessions
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app # Return the Flask application instance

# Check for and create database
def create_database(app):
    if not path.exists(DB_PATH):  # If the database file doesn't exist
        with app.app_context():  # Use the application context
            db.create_all()  # Create all tables in the database
            print('Created database!')  # Print a message confirming database creation
