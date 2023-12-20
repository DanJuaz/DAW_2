from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = 'julio'
DB_PASSWORD = 'Nazaret23+'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    direccion = Column(String)


if __name__ == '__main__':
    usuarios_data = [
        Usuarios(nombre='Julio', edad=23, direccion='Calle 1'),
        Usuarios(nombre='Maria', edad=30, direccion='Avenida 2'),
        Usuarios(nombre='Carlos', edad=25, direccion='Plaza 3'),
        Usuarios(nombre='Luisa', edad=28, direccion='Calle 4'),
        Usuarios(nombre='Pedro', edad=35, direccion='Avenida 5')
    ]

    try:
        # Create all tables in the engine. This is equivalent to "Create Table"
        Base.metadata.create_all(engine)
        # Insertar datos
        session.add_all(usuarios_data)
        # Query datos
        usuarios_list = session.query(Usuarios).all()
        for usuario in usuarios_list:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}, Dirección: {usuario.direccion}")
    except Exception as e:
        print(e)
        session.rollback()
        session.close()
    finally:
        session.commit()
        session.close()
