from flask import Flask,render_template,request,redirect,flash,session,url_for,g
import sqlite3
import hashlib
from flask_bootstrap import Bootstrap
from datetime import datetime,date
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,SelectMultipleField,widgets,SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,URL,Optional,InputRequired
import random

app = Flask(__name__)             # create an application instance called app

app.config['SECRET_KEY'] = 'allahuakbar'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/")
@app.route('/index')
def index():
    #if 'user_name' in session:
    #    return render_template('index.html')
    #return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/buy_nfts')
def buy_nfts():
    return render_template('buy_nfts.html')

@app.route('/buy_coin')
def buy_coin():
    return render_template('buy_coin.html')

@app.route('/cover')
def cover():
    return render_template('cover.html')

if __name__ == "__main__":
    host='127.0.0.1'
    port=8080
    app.run(host,port,debug=True)