from mi_app.folder.model import MESSAGES
from flask import Blueprint
hello = Blueprint('hello', __name__)
@hello.route('/')
@hello.route('/home')
def home():
    return MESSAGES['default']
@hello.route('/index/<key>')
def get_message(key):
    return MESSAGES.get(key) or f"{key} not found!"
@hello.route('/index/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return f"{key} Añadido"
