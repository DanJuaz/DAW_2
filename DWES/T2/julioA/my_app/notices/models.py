"""
DB models for the app
"""
from my_app import db
from wtforms import StringField, DecimalField, SelectField, PasswordField
from flask_wtf import FlaskForm
from decimal import Decimal
from wtforms.validators import InputRequired, NumberRange, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    pwdhash = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        """Check password"""
        return check_password_hash(self.pwdhash, password)

class RegistrationForm(FlaskForm):
    """Registration form"""
    username = StringField('Username', [InputRequired()])
    password = PasswordField(
        'Password', [
            InputRequired(), EqualTo('confirm', message='Passwords must match')
        ]
    )
    confirm = PasswordField('Confirm Password', [InputRequired()])


class LoginForm(FlaskForm):
    """Login form"""
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
