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
#     username = request.form['username']
#     password = request.form['password']
#     user = user.query.filter_by(username=username).first()
#     if user and sha256_crypt.verify(password, user.password):
#         session['logged_in'] = True
#         session['username'] = user.username
#         return redirect(url_for('home'))
#     else:
#         return render_template('home.html', user=user)


# @app.route('/register', methods=["GET", "POST"])
# def register_page():
#     try:
#         form = RegistrationForm(request.form)

#         if request.method == "POST" and form.validate():
#             username = form.username.data
#             email = form.email.data
#             password = sha256_crypt.encrypt((str(form.password.data)))
#             c, conn = connection()

#             x = c.execute("SELECT * FROM users WHERE username = (%s)",
#                           (thwart(username)))

#             if int(x) > 0:
#                 flash("That username is already taken, please choose another")
#                 return render_template('register.html', form=form)

#             else:
#                 c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
#                           (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/")))

#                 conn.commit()
#                 flash("Thanks for registering!")
#                 c.close()
#                 conn.close()
#                 gc.collect()

#                 session['logged_in'] = True
#                 session['username'] = username

#                 return redirect(url_for('dashboard'))

        return render_template("login.html")

    # except Exception as e:
    #     return (str(e))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')