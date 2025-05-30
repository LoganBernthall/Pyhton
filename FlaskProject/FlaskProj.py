#Imports
from pickle import NONE
from flask import Flask, render_template
from requests import Request, Session
import json
import pprint

app = Flask(__name__)
key = ""

@app.route("/")
def index(name=NONE):

    #URL 
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parametersBit = { 'slug': 'bitcoin', 'convert': 'GBP' } 

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key
    }

##Bitcoin#################
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parametersBit)
    infoBitcoin = json.loads(response.text)['data']['1']['quote']['GBP']['price'] 
    print("Bitcoin Price (£):")
    pprint.pprint(infoBitcoin) ##PPrint = pretty print function not a typo!
################### 
##Ethereum################# 

    parametersEth = { 'slug': 'ethereum', 'convert': 'GBP' } 
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parametersEth)
    infoEthereum = json.loads(response.text)['data']['1027']['quote']['GBP']['price'] 
    print("Ethereum Price (£):")
    pprint.pprint(infoEthereum) ##PPrint = pretty print function not a typo!
##Cardano################# 

    parametersC = { 'slug': 'cardano', 'convert': 'GBP' } 
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parametersC)
    infoCardano = json.loads(response.text)['data']['2010']['quote']['GBP']['price'] 
    print("Cardano Price (£):")
    pprint.pprint(infoCardano) ##PPrint = pretty print function not a typo!
################### 
##Dodgecoin################# 

    parametersDog = { 'slug': 'dogecoin', 'convert': 'GBP' } 
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parametersDog)
    infoDog = json.loads(response.text)['data']['74']['quote']['GBP']['price'] 
    print("Dogecoin Price (£):")
    pprint.pprint(infoDog) ##PPrint = pretty print function not a typo!

    return render_template('index.html', name=name, infoBitcoin=infoBitcoin, infoEthereum=infoEthereum, infoCardano=infoCardano, infoDog=infoDog)

        
