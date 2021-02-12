import json
import ccxt
import asyncio
import time
import logging
import logging.config

from datetime import datetime
# import ccxt.async_support as ccxt
import sys, os
os.system('cls')
#####################LOGS INIT###########################
# Log file location
logfile = 'debug.log'
# Define the log format
log_format = (
    '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

# Define basic configuration
logging.basicConfig(
    # Define logging level
    # level=logging.DEBUG,
    # Declare the object we created to format the log messages
    format=log_format,
    # Declare handlers
    handlers=[
        logging.FileHandler(logfile),
        logging.StreamHandler(sys.stdout),
    ]
)

# Define your own logger name
logger = logging.getLogger("Bot")
logger.info('Bot starting')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#######################################################
#####################API INIT###########################
try:
    with open('config.json') as f:
        data = json.load(f)
    exchange = ccxt.crex24 ({
        'apiKey': data["api_key"],
        'secret': data["api_secret"],
    })
except :
    logger.error('APIs not loaded !')
    exit
#######################################################


def place_order(symbol, type, side, amount, price, params): # PARAMS IS DICT
    """
    type = limit/market
    params = {
        'stopPrice': 123.45,  # your stop price
        'type': 'stopLimit',
    }
    """
    order = exchange.create_order(symbol, type, side, amount, price, params)
    
    # orderid = order['id']

def cancel_order(order_id):
    exchange.cancel_order (str(order_id))
    actual_time = datetime.now()
    print(f"Order {order_id} has been closed at {actual_time}")


def main():
    exchange = ccxt.crex24()
    symbols = exchange.symbols   
    # print (exchange.id, symbols) 
    marks = exchange.load_markets()
    # print(json.dumps(marks, indent=4))
    for key,value in marks.items():
        if key == "FDR/BTC" : # or key == "FDR_OLD/BTC"
            crypto_fdr = value
            print(crypto_fdr)
            # print(json.dumps(value, indent=4))
        else:
            pass
    import asyncio
    import ccxt.async_support as ccxtasync
    exchange = ccxtasync.crex24 ({
        'apiKey': data["api_key"],
        'secret': data["api_secret"],
    })



if __name__ == '__main__':
    main()






# {
#     "symbol": "1INCH",
#     "name": "1inch",
#     "isFiat": false,
#     "depositsAllowed": true,
#     "depositConfirmationCount": 12,
#     "minDeposit": 15.0,
#     "withdrawalsAllowed": true,
#     "withdrawalPrecision": 8,
#     "minWithdrawal": 5.0,
#     "maxWithdrawal": 100000000.0,
#     "isDelisted": false
#   },