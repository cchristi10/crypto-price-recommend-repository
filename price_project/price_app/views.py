from django.shortcuts import render
from price_app.rec_price import Price
from price_app.models import BitcoinPrices, EthereumPrices
# Create your views here.
def index(request):
    #Bitcoin
    btc_x1_buy = BitcoinPrices.coinbase_btc_buy_price
    btc_x1_sell = BitcoinPrices.coinbase_btc_sell_price
    btc_x2_buy = BitcoinPrices.gemini_btc_buy_price
    btc_x2_sell = BitcoinPrices.gemini_btc_sell_price


    bitcoin_prices = Price(btc_x1_sell,btc_x1_buy,btc_x2_sell,btc_x2_buy)
    

    if btc_x1_sell == bitcoin_prices.rec_sell_price():
        btc_x1_rec_sell = "Sell Bitcoin"
        btc_x2_rec_sell = ""

    if btc_x2_sell == bitcoin_prices.rec_sell_price():
        btc_x1_rec_sell = ""
        btc_x2_rec_sell= "Sell Bitcoin"

    if btc_x1_buy == bitcoin_prices.rec_buy_price():
        btc_x1_rec_buy = "Buy Bitcoin"
        btc_x2_rec_buy = ""
    if btc_x2_buy ==  bitcoin_prices.rec_buy_price():
        btc_x1_rec_buy = ""
        btc_x2_rec_buy= "Buy Bitcoin"

    #Ethereum
    eth_x1_buy = EthereumPrices.coinbase_eth_buy_price
    eth_x1_sell = EthereumPrices.coinbase_eth_sell_price
    eth_x2_buy = EthereumPrices.gemini_eth_buy_price
    eth_x2_sell = EthereumPrices.gemini_eth_sell_price

    ethereum_prices = Price(eth_x1_sell,eth_x1_buy,eth_x2_sell,eth_x2_buy)

    if eth_x1_sell == ethereum_prices.rec_sell_price():
        eth_x1_rec_sell = "Sell Ethereum"
        eth_x2_rec_sell = ""
    else:
        eth_x1_rec_sell = ""
        eth_x2_rec_sell= "Sell Ethereum"

    if eth_x1_buy == ethereum_prices.rec_buy_price():
        eth_x1_rec_buy = "Buy Ethereum"
        eth_x2_rec_buy = ""
    else:
        eth_x1_rec_buy = ""
        eth_x2_rec_buy= "Buy Ethereum"


    return render(request,'price_app/index.html',{'bitcoin_prices':bitcoin_prices,
                                                'btc_x1_rec_sell':btc_x1_rec_sell,'btc_x2_rec_sell':btc_x2_rec_sell,
                                                'btc_x1_rec_buy':btc_x1_rec_buy, 'btc_x2_rec_buy':btc_x2_rec_buy,
                                                'eth_x1_rec_sell':eth_x1_rec_sell, 'eth_x2_rec_sell':eth_x2_rec_sell,
                                                'eth_x1_rec_buy':eth_x1_rec_buy, 'eth_x2_rec_buy':eth_x2_rec_buy,
                                                'btc_x1_buy':btc_x1_buy,'btc_x1_sell':btc_x1_sell,
                                                'btc_x2_buy':btc_x2_buy,'btc_x2_sell':btc_x2_sell,
                                                'ethereum_prices':ethereum_prices,
                                                'eth_x1_buy':eth_x1_buy,'eth_x1_sell':eth_x1_sell,
                                                'eth_x2_buy':eth_x2_buy,'eth_x2_sell':eth_x2_sell})
