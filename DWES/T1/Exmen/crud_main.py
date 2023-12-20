from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER = 'julio'
DB_PASSWORD = 'Nazaret23+'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    direccion = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_usuario(nombre, edad, direccion):
    usuario = Usuarios(nombre=nombre, edad=edad, direccion=direccion)
    session.add(usuario)
    session.commit()
    return usuario

def read_usuarios():
    return session.query(Usuarios).all()

def update_usuario(usuario_id, new_nombre, new_edad, new_direccion):
    usuario = session.query(Usuarios).get(usuario_id)
    if usuario:
        usuario.nombre = new_nombre
        usuario.edad = new_edad
        usuario.direccion = new_direccion
        session.commit()
        return usuario
    return None

def delete_usuario(usuario_id):
    usuario = session.query(Usuarios).get(usuario_id)
    if usuario:
        session.delete(usuario)
        session.commit()
        return True
    return False

if __name__ == '__main__':
    # Create a user
    create_usuario('Julio', 25, 'Calle 1')

    # Read all users
    usuarios_list = read_usuarios()
    print("All Usuarios:")
    for usuario in usuarios_list:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}, Dirección: {usuario.direccion}")

    # Update a user
    updated_usuario = update_usuario(1, 'Julia', 26, 'Avenida 2')
    if updated_usuario:
        print(f"\nUpdated Usuario:")
        print(f"ID: {updated_usuario.id}, Nombre: {updated_usuario.nombre}, Edad: {updated_usuario.edad}, Dirección: {updated_usuario.direccion}")

    # Delete a user
    deleted = delete_usuario(1)
    if deleted:
        print("\nUsuario Deleted.")

    # Read all users after deletion
    usuarios_list = read_usuarios()
    print("\nUsuarios after Deletion:")
    for usuario in usuarios_list:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}, Dirección: {usuario.direccion}")
