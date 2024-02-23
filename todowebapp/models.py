from . import db  # Import the database instance
from flask_login import UserMixin  # Import UserMixin for user management
from sqlalchemy.sql import func  # Import func for database functions

# User table model
class User(db.Model, UserMixin):
    # Define user table columns
    id = db.Column(db.Integer, primary_key=True)  # User ID column
    email = db.Column(db.String(150), unique=True)  # Email column
    password = db.Column(db.String(150))  # Password column
    firstName = db.Column(db.String(150))  # First name column

    # Establish 1 to many relationship for notes
    notes = db.relationship('Note')  # Relationship with Note table

# Notes table model
class Note(db.Model):
    # Define note table columns
    id = db.Column(db.Integer, primary_key=True)  # Note ID column
    data = db.Column(db.String(10000))  # Note data column
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Date column

    # Establish 1 to many relationship for notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to User table
