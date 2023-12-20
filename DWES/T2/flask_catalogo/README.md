# Documentación de **Flask-migrate**
Intalar modulo:
``
pip install Flask-Migrate
``

Comando inicial
```
PS C:\Users\Daw23\Desktop\DAW_2\DWES\T2\flask_catalogo> flask --app 'run.py' db init
```
Empezando la migración
```
PS C:\Users\Daw23\Desktop\DAW_2\DWES\T2\flask_catalogo> flask --app 'run.py' db migrate -m "Initial migration"
```
Transformando la BD:
```
PS C:\Users\Daw23\Desktop\DAW_2\DWES\T2\flask_catalogo> flask --app 'run.py' db upgrade
```
