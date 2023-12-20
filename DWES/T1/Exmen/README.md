¡Claro! SQLAlchemy proporciona dos formas principales de interactuar con la base de datos: mediante expresiones SQL directas y mediante el uso de modelos de objetos de Python. A continuación, te daré ejemplos de consultas (query), inserciones (insert) y eliminaciones (delete) para ambas formas.

### Interactuar con la base de datos utilizando SQL directo:

#### Consulta (Query):
```python
from sqlalchemy import create_engine, text

# Crear una conexión a la base de datos
engine = create_engine('sqlite:///mi_base_de_datos.db')
conn = engine.connect()

# Ejemplo de consulta SQL
sql_query = text("SELECT * FROM usuarios WHERE edad > :edad")
result = conn.execute(sql_query, edad=25)

# Imprimir resultados
for row in result:
    print(row)

# Cerrar la conexión
conn.close()
```

#### Inserción (Insert):
```python
from sqlalchemy import create_engine, text

# Crear una conexión a la base de datos
engine = create_engine('sqlite:///mi_base_de_datos.db')
conn = engine.connect()

# Ejemplo de inserción SQL
sql_insert = text("INSERT INTO usuarios (nombre, edad) VALUES (:nombre, :edad)")
conn.execute(sql_insert, nombre='Juan', edad=30)

# Confirmar la transacción
conn.commit()

# Cerrar la conexión
conn.close()
```

#### Eliminación (Delete):
```python
from sqlalchemy import create_engine, text

# Crear una conexión a la base de datos
engine = create_engine('sqlite:///mi_base_de_datos.db')
conn = engine.connect()

# Ejemplo de eliminación SQL
sql_delete = text("DELETE FROM usuarios WHERE nombre = :nombre")
conn.execute(sql_delete, nombre='Juan')

# Confirmar la transacción
conn.commit()

# Cerrar la conexión
conn.close()
```

### Interactuar con la base de datos mediante modelos de objetos de Python:

#### Consulta (Query):
```python
from sqlalchemy.orm import sessionmaker
from models import Usuario  # Asumiendo que tienes un modelo de Usuario definido en models.py

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de consulta utilizando modelos de objetos
usuarios_mayores_de_25 = session.query(Usuario).filter(Usuario.edad > 25).all()

# Imprimir resultados
for usuario in usuarios_mayores_de_25:
    print(usuario.nombre, usuario.edad)

# Cerrar la sesión
session.close()
```

#### Inserción (Insert):
```python
from sqlalchemy.orm import sessionmaker
from models import Usuario  # Asumiendo que tienes un modelo de Usuario definido en models.py

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de inserción utilizando modelos de objetos
nuevo_usuario = Usuario(nombre='María', edad=28)
session.add(nuevo_usuario)

# Confirmar la transacción
session.commit()

# Cerrar la sesión
session.close()
```

#### Eliminación (Delete):
```python
from sqlalchemy.orm import sessionmaker
from models import Usuario  # Asumiendo que tienes un modelo de Usuario definido en models.py

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de eliminación utilizando modelos de objetos
usuario_a_eliminar = session.query(Usuario).filter_by(nombre='Juan').first()
session.delete(usuario_a_eliminar)

# Confirmar la transacción
session.commit()

# Cerrar la sesión
session.close()
```

Estos ejemplos asumen que ya tienes configurada una base de datos SQLite con una tabla llamada "usuarios" que tiene columnas como "nombre" y "edad". Asegúrate de adaptar los ejemplos a tu entorno y estructura de base de datos específicos.