####################GET MARKET COMMONS INFOS#################
import json
import ccxt
import asyncio
# import ccxt.async_support as ccxt
import sys, os
os.system('cls')
crex24 = ccxt.crex24()
markets = crex24.load_markets()
print(json.dumps(markets['FDR/BTC'], indent=4))
#############################################################
#####################GET MARKET DEPTH########################
import json
import ccxt
exchange = ccxt.crex24()
limit = 10
test = ccxt.crex24().fetch_order_book('FDR/BTC', limit)
print(json.dumps(test, indent=4))
#############################################################
######################GET BALANCE############################
print (exchange.fetch_balance ())
#############################################################
#####################INVOKE APIs#############################
with open('config.json') as f:
  data = json.load(f)
apik = '\'' + data["api_key"] + '\''
print (apik)
apis = '\'' + data["api_secret"] + '\''
exchange = ccxt.crex24 ({
    'apiKey': data["api_key"],
    'secret': data["api_secret"],
})
#############################################################
########################GET WALLETS##########################
print(json.dumps(exchange.fetch_balance (), indent=4))
#############################################################
#####################LOGS INIT###############################
import logging
import logging.config
# Log file location
logfile = 'debug.log'
# Define the log format
log_format = (
    '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

# Define basic configuration
logging.basicConfig(
    # Define logging level
    level=logging.DEBUG,
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
#############################################################