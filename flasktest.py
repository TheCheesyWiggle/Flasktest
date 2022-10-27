from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__,template_folder='templates', static_folder='staticFiles')

app.secret_key = "Hello fellow programmer"

'''
defines what happens at the route /welcome this allows us to welcome the user
'''
@app.route("/welcome")
def welcome():
    if "user" in session:
        user = session["user"]
        return render_template("welcome.html")
    else:
        return redirect(url_for('login_page'))


'''
defines what happens at the route /login this allows the user to login and us to redirect them to the welcome page
'''
@app.route("/login", methods =['GET','POST'])
def login_page():
    if request.method=='POST':
        user = request.form['username']
        pw = request.form['password']
        session["user"] = user
        login_failed = not login(user, pw)
        if not login_failed:
            if "user" in session:
                return redirect(url_for('welcome'))
    flash("Login failed", "info")            
    return render_template("login.html")

def login(username, password):
    if (username == "finn") and (password=="test"):
        return True
    else:
        return False

'''
defines what happens when you logout
'''
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login_page"))

'''
defines what happens at the route /sign up, this allows the user to create an account
'''
@app.route("/signup")
def signup():
    return "signed up"

'''
defines what happens at the route at the defalt site, gateway to the rest of the website
'''
@app.route("/")
def home():
    return render_template("index.html")

app.run(host="0.0.0.0",port=80)