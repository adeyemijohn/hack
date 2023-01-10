from flask import Flask
from flask.templating import render_template
# from flask import Flask, render_template, flash, request, url_for, redirect, session
# from passlib.hash import sha256_crypt
# from MySQLdb import escape_string as thwart
# import gc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')