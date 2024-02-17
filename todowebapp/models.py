from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# User table model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    fistName = db.Column(db.String(150))
    # Establish 1 to many relationship for notes
    notes = db.relationship('Notes')

# Notes table model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Establish 1 to many relationship for notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))