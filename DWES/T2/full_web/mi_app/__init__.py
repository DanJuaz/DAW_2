from flask import Flask
from mi_app.folder.views import hello
app = Flask(__name__)
app.register_blueprint(hello)
import mi_app.folder.views