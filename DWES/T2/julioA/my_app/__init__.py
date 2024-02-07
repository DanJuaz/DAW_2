""" 
Here I will create the app and the database configurations.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from  my_app.notices.views import notices
from my_app.notices.models import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
# App secret key
app.secret_key = 'key_dwes_2023'
# Credentials for DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://donos_a:Nazaret.23@pgsql03.dinaserver.com:5432/donos_aaaaaaaaaaaaaaaaaaaaaaaa'
db = SQLAlchemy(app)
# Register the blueprints
app.register_blueprint(notices)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    """Load a user"""
    return User.query.get(int(user_id))
