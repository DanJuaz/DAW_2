from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from  mi_app.catalogo.vistas import catalog
# si se pone aquí da un problema de importación circular
# ImportError: cannot import name 'db' from partially 
# initialized module 'mi_app' (most likely due to a circular 
# import). Normal, en vistas se hace import db, todavía no creado.
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'key_dwes_2023'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1:password1@localhost/eval2'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from  mi_app.catalogo.vistas import catalog
app.register_blueprint(catalog)
with app.app_context():
    db.create_all()