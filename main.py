from flask import Flask
import os
from web3 import Web3

app = Flask(__name__)

@app.route('/')
def default():
   bsc = "https://bsc-dataseed.binance.org/"
   web3 = Web3(Web3.HTTPProvider(bsc))
   print(web3.isConnected())

   return "Test"
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
   #app.run()
