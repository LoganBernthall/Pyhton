from pickle import NONE
from flask import Flask, render_template
from requests import Request, Session
import json
import pprint

app = Flask(__name__)
key = "17cf1c41-d5ae-4446-84fe-fd5b7394fb26"

@app.route("/")
def index(name=NONE):
    return render_template('index.html', name=name)

@app.route('/')
def GetBitcoin():

    #URL 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'bitcoin', 'convert': 'GBP' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    infoBitcoin = json.loads(response.text)['data']['1']['quote']['GBP']['price'] 
    
    print("Bitcoin Price (£):")
    pprint.pprint(infoBitcoin)
        
GetBitcoin()

def GetEthereum():

    #URL 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'ethereum', 'convert': 'GBP' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    infoEthereum = json.loads(response.text)['data']['1027']['quote']['GBP']['price'] 
    
    print("Ethereum Price (£):")
    pprint.pprint(infoEthereum)

GetEthereum()

def GetCardano():

    #URL 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'cardano', 'convert': 'GBP' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    infoCardano = json.loads(response.text)['data']['2010']['quote']['GBP']['price'] 
    
    print("Cardano Price (£):")
    pprint.pprint(infoCardano)

GetCardano()