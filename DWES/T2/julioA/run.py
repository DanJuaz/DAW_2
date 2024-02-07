"""APP run file"""
from my_app import app
if __name__ == '__main__':
    app.env='venv'
    app.run(debug=True)
