from mi_app import app, db
from flask_migrate import Migrate
from random import randint
from mi_app.catalogo.model import Product, Category

migrate = Migrate(app, db)
app.secret_key = 'key_dwes_2023'

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        """
        print("Creando productos...")
                
        nombres = ["Black Berry", "Silla", "Lapiz", "ASUS 5000", "Mochila", "Cazadora", "Nike Air force", "Cascos"]
        precios = [5.99, 12.99, 29.95, 65.65, 10.00]
        categorias = ["Tecnologia", "Mobiliario", "Ropa", "Zapatos", "Portatiles"]

        def get_random_nombres():
            return randint(0, len(nombres) - 1)

        def get_random_precios():
            return randint(0, len(precios) - 1)

        def get_random_categorias():
            return randint(0, len(categorias) - 1)

        created_products = []

        i = 0
        while i < 30:
            nombre = nombres[get_random_nombres()]
            precio = precios[get_random_precios()]
            categoria_name = get_random_categorias()
            existing_product = (
                db.session.query(Product)
                .filter_by(name=nombre, price=precio)
                .join(Category)
                .filter_by(name=categorias[categoria_name])
                .first()
            )
            if existing_product is None:
                categoria_name = categorias[categoria_name]
                category_existing = (
                    db.session.query(Category).filter_by(name=categoria_name).first()
                )
                if category_existing is None:
                    category = Category(categoria_name)
                    db.session.add(category)
                    db.session.commit()
                    category_id = category.id
                else:
                    category_id = category_existing.id

                product = Product(nombre, precio, category_id)
                db.session.add(product)
                db.session.commit()
                created_products.append((nombre, precio, categoria_name))
                i += 1
            else:
                print("Product already exists")

        print(created_products)
        print(len(created_products))
    """

