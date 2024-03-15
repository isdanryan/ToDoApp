from dotenv import load_dotenv  # Use dotenv to load enviroment variables
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
# Get the directory name of the database file
directory = path.dirname(DB_PATH)


def create_app(db_uri=None):
    # Create Flask application instance
    app = Flask(__name__)
    # Set the secret key for the Flask app
    app.config['SECRET_KEY'] = SECRET_KEY
    # If statement to set database URI if not testing
    if db_uri:
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            f'sqlite:///{path.abspath(DB_PATH)}'  # Set the database URI
    # Initialize the database with the Flask app
    db.init_app(app)

    # Import routes
    from .views import views
    # Register the views blueprint with the app
    app.register_blueprint(views, url_prefix='/')

    # Import database structure from models.py
    from .models import User

    create_database(app)

    # Create LoginManager instance
    login_manager = LoginManager()

    # Set the login view for the LoginManager
    login_manager.login_view = 'views.login'

    # Initialize LoginManager with the Flask app
    login_manager.init_app(app)

    # Use flask_login to check for and manage user sessions
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app  # Return the Flask application instance


# Check for and create database
def create_database(app):
    if not path.exists(DB_PATH):
        with app.app_context():
            db.create_all()
            print('Created database!')
