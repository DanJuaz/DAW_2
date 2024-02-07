from flask  import request, jsonify, Blueprint
from mi_app import db, login_manager
from mi_app.catalogo.modelos import Product, Category, User
from mi_app.catalogo.modelos import ProductForm, LoginForm, RegistrationForm
from flask import render_template
from flask import flash
from flask import redirect, url_for
from flask_login import current_user, login_user, logout_user, \
    login_required


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

catalog = Blueprint('catalog',__name__)

'''
Esto es por una duda que me preguntó Efren
@catalog.route('/one-request')
def request_one():
    prod = request.args.get('silla', 'producto')    
    return f'A simple Flask request where argument is {prod}'
# ejemplo url: http://127.0.0.1:5000/one-request?silla=taburete
# resultado: 'A simple Flask request where argument is taburete'

@catalog.route('/one-request/<silla>')
def request_two(silla):
    return f'A simple Flask request where argument is {silla}'
# ejemplo url: http://127.0.0.1:5000/one-request/taburete
# resultado: 'A simple Flask request where argument is taburete'
'''

@catalog.route('/')
@catalog.route('/home')
def home():
    return render_template('home.html')


@catalog.route('/product/<int:id>')
@login_required
def product(id):
    product = Product.query.get_or_404(id)        
    return render_template('producto.html', product=product)


@catalog.route('/products')
@catalog.route('/products/<int:page>')
@login_required
def products(page=1):
    products = Product.query.paginate(page=page, per_page=3)    
    return render_template('products.html', products=products)
    #products = Product.query.all()
    #products = Product.query.paginate(page=page, per_page=10).items    
    '''
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
            'category': product.category.name
        }
    return jsonify(res)
    '''

@catalog.route('/product-create', methods=['GET','POST'])
@login_required
def create_product():
    form = ProductForm(meta={'csrf': False})
    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices = categories
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        category = Category.query.get_or_404(form.category.data)        
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        flash(f'The product {name} has been created', 'success')
        return redirect(url_for('catalog.product', id=product.id))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('crear_producto.html', form=form)
    '''
    name = request.form.get('name')
    price = request.form.get('price')
    categName = request.form.get('category')
    category = Category.query.filter_by(name=categName).first()
    if not category:
        category = Category(categName)
    product = Product(name,price,category)    
    db.session.add(product)
    db.session.commit()
    #return 'Product created.'
    return render_template('producto.html', product=product)
    '''

@catalog.route('/category-create', methods=['GET'])
# ejemplo url: http://127.0.0.1:5000/category-create?name=nuevaCategory
@login_required
def create_category():
    name = request.args.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    #return 'category created'
    return render_template('category.html', category=category)

@catalog.route('/category/<id>')
@login_required
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)

@catalog.route('/categories')
@login_required
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)
    '''
    res = {}
    for category in categories:
        res[category.id] = {
            'name': category.name
        }
        res[category.id]['products']=[]
        for product in category.products:
            res[category.id]['products'].append({
                'id': product.id,
                'name': product.name,
                'price': product.price                
            })
    return jsonify(res)
    '''

@catalog.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('catalog.home'))

    form = LoginForm()
    # Si no ponemos form = LoginForm(meta={'csrf': False})
    # luego en los html habrá que añadir al formulario
    # {{ form.csrf_token }}

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()

        if not (existing_user and existing_user.check_password(password)):
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html', form=form)

        login_user(existing_user, remember=True)
        flash('You have successfully logged in.', 'success')
        return redirect(url_for('catalog.products'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)

@catalog.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('catalog.home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash(
                'This username has been already taken. Try another one.',
                'warning'
            )
            return render_template('register.html', form=form)
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered. Please login.', 'success')
        return redirect(url_for('catalog.login'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('register.html', form=form)

@catalog.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('catalog.home'))
