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


@app.route("/")
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    if 'user_name' in session:
        return render_template('index.html')
    return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/BuyNFTs')
def BuyNFTs():
    return render_template('BuyNFTs.html')

@app.route('/BuyCoin')
def BuyCoin():
    return render_template('BuyCoin.html')



if __name__ == "__main__":
    host='127.0.0.1'
    port=8080
    app.run(host,port,debug=True)