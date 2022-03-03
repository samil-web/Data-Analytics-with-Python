from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def signup_page():
    if request.method == "POST":
        email = request.form["email"]
        return redirect(url_for("e_adress",mail=email))
    else:
        return render_template("signup.html")

@app.route("/<mail>",methods=["GET","POST"])
def e_adress(mail):
    return render_template('base.html',content='{}'.format(mail))

# @app.route("/greet",methods=["GET","POST"])
# def greet():
#     if request.method == "POST":
#         email_add = request.form.get("email")
#         return render_template("greet.html",email_add=email_add)
#     else:
#         return render_template('signup.html')