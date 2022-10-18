from flask import Flask, render_template,request,redirect
import requests
import json

app = Flask(__name__)
username = ""

def login(username, password):
    if (username == "test") and (password =="test"):
            username = "test"
            return redirect("/welcome")
    return render_template("index.html")

@app.route("/welcome",)
def welcome():
    return render_template("welcome.html",username=username)

@app.route("/login", methods =['GET','POST'])
def login_page():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
    login(username, password)
    return render_template("login.html")

@app.route("/")
def home():
    return render_template("index.html")

app.run(host="0.0.0.0",port=80)