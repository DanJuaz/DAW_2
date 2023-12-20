from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Modelo SQLAlchemy
Base = declarative_base()

class PersonaModel(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    direccion = Column(String)

# Función para convertir PersonaModel a diccionario
def persona_model_a_diccionario(persona_model):
    return {
        'nombre': persona_model.nombre,
        'edad': persona_model.edad,
        'direccion': persona_model.direccion
    }

# Configuración de la base de datos
config = cargar_configuracion()
engine = create_engine(
    f"postgresql://{config['database']['username']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}/{config['database']['database_name']}"
)

# Crear tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)

# Función para insertar personas en la base de datos
def insertar_personas(personas):
    with Session() as session:
        for persona in personas:
            nuevo_usuario = PersonaModel(nombre=persona['nombre'], edad=persona['edad'], direccion=persona['direccion'])
            session.add(nuevo_usuario)

        # Confirmar la transacción
        session.commit()

# Función para recuperar todas las personas de la base de datos y mostrarlas
def obtener_personas():
    with Session() as session:
        personas = session.query(PersonaModel).all()

        for persona in personas:
            print(persona_model_a_diccionario(persona))

# Cargar configuración desde config.json
def cargar_configuracion():
    try:
        with open('config.json') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("Archivo de configuración no encontrado.")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar el archivo de configuración JSON.")
        return None


