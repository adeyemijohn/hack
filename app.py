from flask import Flask, request
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def home():
    if request.method == 'POST':
        if request.form['order_online']:
            render_template('login.html')
        else:
            request.method == 'GET'
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')