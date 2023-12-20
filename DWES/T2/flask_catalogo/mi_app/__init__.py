from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = 'catalog.login'
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://user1:password1@localhost/eval1'
db = SQLAlchemy(app)


from mi_app.catalogo.views import catalog
app.register_blueprint(catalog)
with app.app_context():
    db.create_all()
