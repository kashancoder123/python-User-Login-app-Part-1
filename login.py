from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"  # required for session

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Rz8hqn1dK4",
            password="p3J4h3Y9hE",
            database="Rz8hqn1dK4"
        )
        cursor = mydb.cursor()
        cursor.execute(
            "SELECT * FROM LoginDetails WHERE username=%s AND password=%s",
            (username, password)
        )
        account = cursor.fetchone()

        if account:
            session['username'] = username
            msg = "Logged in successfully"
            return render_template("index.html", name=username, msg=msg)
        else:
            msg = "Incorrect credentials. Kindly check."

    return render_template("login.html", msg=msg)


# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    msg = "Logged out successfully"
    return render_template("login.html", msg=msg)


# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Rz8hqn1dK4",
            password="p3J4h3Y9hE",
            database="Rz8hqn1dK4"
        )
        cursor = mydb.cursor()
        cursor.execute(
            "INSERT INTO LoginDetails (username, password, email) VALUES (%s, %s, %s)",
            (username, password, email)
        )
        mydb.commit()
        msg = "Registration successful! Please login."

    return render_template("register.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
