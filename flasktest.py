from urllib import response
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    x = "Hello world"
    return render_template("index.html", x=x)

app.run(host="0.0.0.0",port=80)