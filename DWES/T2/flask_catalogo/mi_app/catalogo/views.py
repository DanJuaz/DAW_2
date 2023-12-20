from flask import render_template, request, jsonify, Blueprint, redirect, url_for, flash
from mi_app.catalogo.model import Product, Category, User, ProductForm, LoginForm, RegisterForm, CategoryForm
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from mi_app import login_manager, db

catalog = Blueprint('catalog', __name__)


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None


@catalog.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'csrf': False})
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')

        # Check if the username already exists
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.pwdhash, password):
                if not remember_me:
                    login_user(user)  # Save the user session
                    flash('Login successful', 'success')
                else:
                    # Remember me cookies -> 1Y
                    login_user(user, True)
                return redirect(url_for('catalog.products'))
            else:
                flash('Invalid username or password', 'danger')
                return redirect(url_for('catalog.login'))
        else:
            flash('User does not exist', 'danger')
            return redirect(url_for('catalog.register'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form, current_user=current_user)


@catalog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={'csrf': False})
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')


        # Check if the username already exists
        existing_user = User.query.filter_by(name=username, email=email).first()
        if existing_user:
            flash('This username is already taken', 'danger')
            return redirect(url_for('catalog.register'))

        # If the username is not taken, create a new user
        user = User(name=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully', 'success')
        return redirect(url_for('catalog.login'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('register.html', form=form, current_user=current_user)



@catalog.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('catalog.home'))


@catalog.route('/')
@catalog.route('/home')
def home():
    products_q = Product.query.all()
    print(products_q)
    return render_template('home.html', products=products_q, current_user=current_user)


@catalog.route('/product/<id>')
@login_required
def product(id):
    product = Product.query.get_or_404(id)
    print(f"Product: {product.name} - Price: {product.price}")
    return render_template('product.html', product=product, current_user=current_user)


@catalog.route('/products')
@catalog.route('/products/<int:page>')
@login_required
def products(page=1):
    per_page = 6
    products_pagination = Product.query.paginate(page=page, per_page=per_page)

    products = products_pagination.items
    total_pages = products_pagination.pages

    return render_template('products.html', products=products, current_page=page, total_pages=total_pages, current_user=current_user)


@catalog.route('/product-create', methods=['POST', 'GET'])
@login_required
def create_product():
    form = ProductForm(meta={'csrf': False})

    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices = categories
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category_id = Category.query.get_or_404(request.form.get('category'))
        product = Product(name=name, price=price, category_id=category_id.id)
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully', 'success')
        return redirect(url_for('catalog.product', id=product.id))

    if form.errors:
        flash(form.errors, 'danger')
    return render_template('crear_producto.html', form=form, current_user=current_user)

"""
Para el que se anime, implementar la posibilidad de añadir una
categoría nueva o seleccionar una existente.
"""
@catalog.route('/category-create', methods=['POST', 'GET'])
@login_required
def category_create():
    form = CategoryForm(meta={'csrf': False})
    if request.method == 'POST':
        name_category = request.form.get('name')
        existing_category = Category.query.filter_by(name=name_category).first()
        print(existing_category)

        if not existing_category:
            new_category = Category(name=name_category)
            db.session.add(new_category)
            db.session.commit()
            flash('The category has created successfully', 'success')
            return redirect(url_for('catalog.create_product'))
        else:
            flash('The category already exits', 'danger')
            return redirect(url_for('catalog.create_product'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('crear_categoria.html', form=form, current_user=current_user)



@catalog.route('/category/<id>')
@login_required
def category(id):
    category = Category.query.get_or_404(id)
    products = Product.query.filter_by(category_id=id).all()
    print(category.name, category.id, category)
    return render_template('category.html', category=category, products=products, current_user=current_user)


@catalog.route('/categories', )
@login_required
def categorys():
    categories = Category.query.all()
    """    res = {}
    for category in categories:
        res[category.id] = {
            'name': category.name,
            'products': [
                {
                    'id': str(product.id),
                    'name': product.name,
                    'price': str(product.price)
                } for product in category.products
            ]
        }
    #return jsonify(res)"""
    return render_template('categories.html', categories=categories, current_user=current_user)



