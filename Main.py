from flask import Flask,render_template,request,redirect,flash,session,url_for,g
import sqlite3
import hashlib
import ssl
from datetime import datetime,date

import random

app = Flask(__name__)             # create an application instance called app

app.config['SECRET_KEY'] = 'allahuakbar'




def con_db():
    con=sqlite3.connect("C:\\Users\\Administrator\\Documents\\GitHub\\SolarNFT\\Solar.db",check_same_thread=False)
    con.row_factory=sqlite3.Row
    return con


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []

sql = """
                select user_name,password
                from User
                """
cur = con_db().cursor()
cur.execute(sql)
result=cur.fetchall()

for i in result:
    users.append(User(username=i[0], password=i[1]))


@app.route('/cover',methods=['GET', 'POST'])
def cover():
    print(request.method)
    if request.method == 'POST':
        username = request.form['inputUsername']
        password = request.form['inputPassword']
        user_index = None
        for i in users:
            if str(i.username) == str(username):
                user_index = users.index(i)
                break

        if user_index == None:
            return render_template('cover.html')
        if users[user_index].password == password:
            session['user_name'] = users[user_index].username
            return redirect(url_for('index'))

        return redirect(url_for('cover'))

    return render_template('cover.html')

@app.route("/",methods=['GET', 'POST'])
@app.route('/index')
def index():
    if 'user_name' in session:
        return render_template('index.html',page="index")
    return redirect(url_for('cover'))

@app.route('/buy_nfts')
def buy_nfts():
    if 'user_name' in session:
        return render_template('buy_nfts.html',page="buy_nfts")
    return redirect(url_for('cover'))


@app.route('/buy_coin')
def buy_coin():
    if 'user_name' in session:
        return render_template('buy_coin.html',page="buy_coin")
    return redirect(url_for('cover'))

@app.route('/option_yield')
def option_yield():
    if 'user_name' in session:
        return render_template('option_yield.html',page='option_yield')
    return redirect(url_for('cover'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('cover'))

@app.route('/my_nfts')
def my_nfts():
    if 'user_name' in session:
        return render_template('my_nfts.html',page="my_nfts")
    return redirect(url_for('cover'))

@app.route('/wallet')
def wallet():
    if 'user_name' in session:
        return render_template('wallet.html',page="wallet")
    return redirect(url_for('cover'))

@app.route('/register_nfts')
def register_nfts():
    if 'user_name' in session:
        return render_template('register_nfts.html',page="register_nfts")
    return redirect(url_for('cover'))

@app.route('/my_coin')
def my_coin():
    if 'user_name' in session:
        return render_template('my_coin.html',page="my_coin")
    return redirect(url_for('cover'))


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)


context.load_cert_chain("C:\\Users\\Administrator\\Documents\\GitHub\\SolarNFT\\certificate.crt", "C:\\Users\\Administrator\\Documents\\GitHub\\SolarNFT\\private.key")

if __name__ == "__main__":
    host='192.168.0.198'
    port=5000
    app.run(host,port,debug=True,ssl_context=context)

    #,ssl_context=('C:\\Users\\Administrator\\Documents\\GitHub\\SolarNFT\\cert.pem', 'C:\\Users\\Administrator\\Documents\\GitHub\\SolarNFT\\key.pem')