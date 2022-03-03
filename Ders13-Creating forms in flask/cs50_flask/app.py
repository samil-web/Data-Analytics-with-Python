from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("greet.html")

@app.route("/signup",methods=["POST"])
def signup():
    email = request.form['email']
    return render_template('base.html',email=email)

@app.route("/greet",methods=["GET","POST"])
def greet_user():
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    fullname = " ".join((first_name, last_name))
    greeting_phrase = f"Hello, guys! I'm {fullname}"
    return greeting_phrase