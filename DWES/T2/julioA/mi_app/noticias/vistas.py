"""
Views for the app
"""
from flask import request, Blueprint
from mi_app import db, login_manager
from mi_app.noticias.modelo import Usuario, Noticia
from mi_app.noticias.modelo import FormLogin, FormRegistro, FormNoticia
from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_user, logout_user, \
    login_required

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

news = Blueprint('news',__name__)

@news.route('/')
@news.route('/home')
def home():
    """Home view"""
    return render_template('home.html')

# User views
@news.route('/login', methods=['GET', 'POST'])
def login():
    """Login a user"""
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('news.home'))

    form = FormLogin()

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = Usuario.query.filter_by(username=username).first()

        if not (existing_user and existing_user.check_pass(password)):
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html', form=form)

        login_user(existing_user, remember=True)
        flash('You have successfully logged in.', 'success')
        return redirect(url_for('news.noticias'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)

@news.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user"""
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('news.home'))

    form = FormRegistro()

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_username = Usuario.query.filter_by(username=username).first()
        if existing_username:
            flash(
                'This username has been already taken. Try another one.',
                'warning'
            )
            return render_template('registro.html', form=form)
        user = Usuario(username, password)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered. Please login.', 'success')
        return redirect(url_for('news.login'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('registro.html', form=form)

@news.route('/logout')
@login_required
def logout():
    """Logout a user"""
    logout_user()
    return redirect(url_for('news.home'))

# Notices views

@news.route('/news')
@news.route('/news/<int:page>')
@login_required
def noticias(page=1):
    notices = Noticia.query.paginate(page=page, per_page=3)
    return render_template('noticias.html', notices=notices)


@news.route('/crear-noticia', methods=['GET','POST'])
@login_required
def crear_noticia():
    form = FormNoticia(meta={'csrf': False})

    if form.validate_on_submit():
        title = form.title.data
        resumen = form.resumen.data
        notice = Noticia(title, resumen)
        db.session.add(notice)
        db.session.commit()
        flash(f'The Notice {title} has been created', 'success')
        return redirect(url_for('news.noticias', id=notice.id))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('crear_noticia.html', form=form)