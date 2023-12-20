from mi_app import db
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, PasswordField, EmailField, validators, BooleanField
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import InputRequired, NumberRange


class ProductForm(FlaskForm):
    name = StringField('Nombre', validators=[InputRequired()])
    price = FloatField('Precio', validators=[InputRequired(), NumberRange(min=0.0, max=9999.99)])
    category = SelectField('Categoría', validators=[InputRequired()], coerce=int)


class CategoryForm(FlaskForm):
    name = StringField(' Category Nombre', validators=[InputRequired()])


class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField("Remember Me")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), validators.Length(max=50)])



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pwdhash = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, password, email):
        self.name = name
        self.pwdhash = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

    def __repr__(self):
        return f"<Product {self.id}>"
