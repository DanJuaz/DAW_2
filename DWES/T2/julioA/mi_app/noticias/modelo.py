"""
DB models for the app
"""
from mi_app import db
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    clave = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.clave = generate_password_hash(password)

    def check_pass(self, password):
        """Check password"""
        return check_password_hash(self.clave, password)

class Noticia(db.Model):
    """Notice Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    resumen = db.Column(db.String(250))

    def __init__(self, title, resumen):
        self.title = title
        self.resumen = resumen
    def __repr__(self):
        return f'<Notice {self.id}>'

class FormNoticia(FlaskForm):
    """Notice Form"""
    title = StringField('Title', [InputRequired()])
    resumen = StringField('Resumen', [InputRequired()])

class FormRegistro(FlaskForm):
    """Registration form"""
    username = StringField('Username', [InputRequired()])
    password = PasswordField(
        'Password', [
            InputRequired(), EqualTo('confirm', message='Passwords must match')
        ]
    )
    confirm = PasswordField('Confirm Password', [InputRequired()])


class FormLogin(FlaskForm):
    """Login form"""
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
