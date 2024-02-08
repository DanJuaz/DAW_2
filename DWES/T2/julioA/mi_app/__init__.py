from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'key_dwes_2023'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:password1@localhost/eval2'
db = SQLAlchemy(app)

from mi_app.noticias.vistas import news
app.register_blueprint(news)

with app.app_context():
    db.create_all()
