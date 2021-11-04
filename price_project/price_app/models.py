from django.db import models
import requests, json
import time
from datetime import datetime


#Coinbase Exchange
coinbase_btc_buy_url = "https://api.coinbase.com/v2/prices/BTC-USD/buy"
coinbase_btc_sell_url = "https://api.coinbase.com/v2/prices/BTC-USD/sell"
coinbase_eth_buy_url = "https://api.coinbase.com/v2/prices/ETH-USD/buy"
coinbase_eth_sell_url = "https://api.coinbase.com/v2/prices/ETH-USD/sell"

response1 = requests.get(coinbase_btc_buy_url)
response2 = requests.get(coinbase_btc_sell_url)
response3 = requests.get(coinbase_eth_buy_url)
response4 = requests.get(coinbase_eth_sell_url)

btc_buy_price = response1.json()
btc_sell_price = response2.json()
eth_buy_price = response3.json()
eth_sell_price = response4.json()

#Gemini Exchange
base_url = "https://api.gemini.com/v1"
btc_response = requests.get(base_url + "/pubticker/btcusd")
btc_data = btc_response.json()
eth_response = requests.get(base_url + "/pubticker/ethusd")
eth_data = eth_response.json()

class BitcoinPrices:
    coinbase_btc_buy_price = btc_buy_price['data']['amount']
    coinbase_btc_sell_price = btc_sell_price['data']['amount']
    gemini_btc_buy_price = btc_data['bid']
    gemini_btc_sell_price =btc_data['ask']


    def __str__(self):

        return "coinbase_btc_buy_price: " + btc_buy_price['data']['amount'] + "\ncoinbase_btc_sell_price: " +btc_sell_price['data']['amount']+"\ngemini_btc_buy_price: " + btc_data['bid']+"\ngemini_btc_sell_price: "+ btc_data['ask']




class EthereumPrices:
    coinbase_eth_buy_price = eth_buy_price['data']['amount']
    coinbase_eth_sell_price = eth_sell_price['data']['amount']
    gemini_eth_buy_price = eth_data['bid']
    gemini_eth_sell_price = eth_data['ask']


    def __str__(self):
        return "coinbase_eth_buy_price: "+eth_buy_price['data']['amount']+"\ncoinbase_eth_sell_price: "+eth_sell_price['data']['amount']+"\ngemini_eth_buy_price: "+eth_data['bid']+"\ngemini_eth_sell_price: "+eth_data['ask']
if __name__ == '__main__':

    print(BitcoinPrices())
    print(" ")
    print(EthereumPrices())
