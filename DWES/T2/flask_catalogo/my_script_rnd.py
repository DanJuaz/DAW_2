from random import randint
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URI = 'postgresql://user1:password1@localhost/eval1'
engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref='products')

    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

    def __repr__(self):
        return f"<Product {self.id}>"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# Close the session
session.close()
