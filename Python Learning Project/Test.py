from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/basics")
def basics():
    return render_template('basics.html')

@app.route("/uses")
def uses():
    return render_template('uses.html')
    
@app.route("/libraries")
def libraries():
    return render_template('libraries.html')

@app.route("/credit")
def credit():
    return render_template('credit.html')