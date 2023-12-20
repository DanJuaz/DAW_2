from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Configurar la conexión a la base de datos PostgreSQL
engine = create_engine('postgresql://usuario:contraseña@localhost/nombre_de_la_bd')

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
def abrir_sesion():
    return Session()

def cerrar_sesion(session):
    # Cerrar la sesión al terminar
    session.close()

class miCRUD:
    def create(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def read(cls, session, **consulta):
        # return session.query(cls).filter_by(**consulta).first()
        return session.query(cls).all()

    def update(self,session):
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()


Base = declarative_base()
# Clase que representa la tabla 'productos'
class Producto(Base, miCRUD):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    producto = Column(String)
    modelo = Column(String)
    precio = Column(Float)
    
# Crear la tabla en la base de datos (esto solo se hace una vez)
Base.metadata.create_all(engine)

'''
# Ejemplo de uso:

for i in range(1,4):
    # crear una nueva instancia de Producto en cada iteración del bucle, de modo que cada instancia tenga su propio valor de id
    product = Producto()
    product.producto = f"Producto{i}"
    product.modelo = f"Modelo{i}"
    product.precio = 90-4*i
    product.create()  # Crear un nuevo producto

# de otra manera:
product = Producto(producto='Producto4', modelo='Modelo4', precio=99.55)
product.create()  # Crear un nuevo producto

# Leer un producto por ID
consulta = {"id": 2}
product = Producto.read(**consulta)
print(product.producto, product.modelo, product.precio)

# Actualizar el producto encontrado (id=2)
product.producto = 'NuevoProducto2'
product.update()

# Borrar el producto con id=3
consulta = {"id": 3}
product = Producto.read(**consulta)
product.delete()
'''