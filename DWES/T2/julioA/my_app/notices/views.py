from flask  import request, jsonify, Blueprint
from my_app.notices.models import LoginForm, RegistrationForm
from flask import render_template
from flask import flash
from flask import redirect, url_for
from flask_login import current_user, login_user, logout_user, \
    login_required


notices = Blueprint('catalog',__name__)

@notices.route('/login', methods=['GET', 'POST'])
def login():
    """Login a user"""
    if current_user.is_authenticated:
        flash('You are already logged in.', 'info')
        return redirect(url_for('catalog.home'))

    form = LoginForm()

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()

        if not (existing_user and existing_user.check_password(password)):
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html', form=form)

        login_user(existing_user, remember=True)
        flash('You have successfully logged in.', 'success')
        return redirect(url_for('notices.products'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)

@notices.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user"""
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

@notices.route('/logout')
@login_required
def logout():
    """Logout a user"""
    logout_user()
    return redirect(url_for('notices.home'))
