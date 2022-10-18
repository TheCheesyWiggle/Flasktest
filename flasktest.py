from flask import Flask, render_template, request, redirect

app = Flask(__name__)
user = "default"

def login(username, password):
    if (username == "Finn") and (password=="test"):
            username = "test"
            return True
    else:
        return False

@app.route("/welcome")
def welcome():
    return render_template("welcome.html",username=user)

@app.route("/login", methods =['GET','POST'])
def login_page():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        if login(username, password):
            print("hello")
            global user 
            user = username
            redirect('/welcome')
    return render_template("login.html", login_failed = False)

@app.route("/")
def home():
    return render_template("index.html")

app.run(host="0.0.0.0",port=80)