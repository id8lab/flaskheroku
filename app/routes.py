import os
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from urllib.parse import quote_plus
from pymongo import MongoClient


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Singapore!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]


    post_data = {
    'user': 'Michael Hansen',
    'email': 'michaelhansen@vizneo.com',
    'password': '123'
     }
    client = MongoClient(os.environ.get('MLABURI'))
    collection = client[os.environ.get('MLABDB')].herokudb
    collection.insert_one({"title": "Test"})
    client.close(); 
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)