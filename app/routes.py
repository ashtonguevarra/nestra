from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from sqlalchemy as sa 
from app import db
from app.models import User 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ashton'}
    posts = [
        {
            'author': {'username': 'Dom'},
            'body': 'I pissed my pants today.'
        },
        {
            'author': {'username': 'Tonee'},
            'body': 'I think I have a crush on Ashton.'
        },
        {
            'author': {'username': 'Pau'},
            'body': 'so uhh we broke up...'
        },
        {
            'author': {'username': 'Drei'},
            'body': 'best night ever with robie!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        if user is None or not user.check_password (form.password.data)
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash('Login requested for user {}, remember_me={}'.format(form.username.date, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


