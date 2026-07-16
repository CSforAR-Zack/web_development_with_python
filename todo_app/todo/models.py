import datetime as dt

import flask_login as fl

from todo.extensions import db


class User(db.Model, fl.UserMixin):
    """User model representing a user in the system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Task(db.Model):
    """Task model representing a task in the system."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    start_time = db.Column(db.DateTime, nullable=False, default=lambda: dt.datetime.now(dt.timezone.utc))
    completed_date = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


