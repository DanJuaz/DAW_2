Aquí te dejo un ejemplo básico de cómo usar SQLAlchemy con Flask para realizar operaciones de inserción, eliminación y actualización en una base de datos. Este ejemplo asume que ya tienes Flask y SQLAlchemy instalados en tu entorno de desarrollo:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        username = request.json.get('username', user.username)
        email = request.json.get('email', user.email)
        user.username = username
        user.email = email
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

En este ejemplo, definimos un modelo de usuario (`User`) con tres atributos: `id`, `username` y `email`. Luego, definimos tres rutas en nuestra aplicación Flask para realizar las operaciones CRUD:

1. `/create_user` - POST: Permite crear un nuevo usuario enviando un JSON con el nombre de usuario y el correo electrónico.
2. `/delete_user/<user_id>` - DELETE: Permite eliminar un usuario existente por su ID.
3. `/update_user/<user_id>` - PUT: Permite actualizar los detalles de un usuario existente por su ID, enviando un JSON con los nuevos valores de `username` y/o `email`.

Recuerda que este es solo un ejemplo básico y que en un entorno de producción deberías considerar aspectos de seguridad y validación adicionales. Además, es importante manejar adecuadamente los errores y excepciones que puedan surgir durante estas operaciones.