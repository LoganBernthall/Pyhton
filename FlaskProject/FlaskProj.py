from pickle import NONE
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(name=NONE):
    return render_template('index.html', name=name)