from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
user = "default"

def login(username, password):
    if (username == "finn") and (password=="test"):
            return True
    else:
        return False

#defines what happens at the route /welcome this allows us to welcome the user
@app.route("/welcome")
def welcome():
    if user != "default":
        return render_template("welcome.html",username=user)
    else:
        return redirect(url_for('login_page'))

#defines what happens at the route /login this allows the user to login and us to redirect them to the welcome page
@app.route("/login", methods =['GET','POST'])
def login_page():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        login_failed = not login(username, password)
        if not login_failed:
            global user 
            user = username
            return redirect(url_for('welcome'))
        else:
            return render_template("login.html", login_f = True)
    return render_template("login.html", login_f = True)

#defines what happens at the route /sign up, this allows the user to create an account
@app.route("/signup")
def signup():
    return "signed up"

#defines what happens at the route at the defalt site, gateway to the rest of the website
@app.route("/")
def home():
    return render_template("index.html")

app.run(host="0.0.0.0",port=80)