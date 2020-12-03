# IMPORTATIONS
import json
import logging
import quotecast.helpers.pb_handler as pb_handler

from IPython.display import display
from trading.api import API as TradingAPI
from trading.pb.trading_pb2 import Credentials, ProductSearch

# SETUP LOGGING LEVEL
logging.basicConfig(level=logging.DEBUG)

# SETUP CONFIG DICT
with open('config/config.json') as config_file:
    config_dict = json.load(config_file)

# SETUP CREDENTIALS
int_account = config_dict['int_account']
username = config_dict['username']
password = config_dict['password']
credentials = Credentials(
    int_account=int_account,
    username=username,
    password=password,
)

# SETUP TRADING API
trading_api = TradingAPI(credentials=credentials)

# ESTABLISH CONNECTION
trading_api.connection_storage.connect()

# PREPARE REQUESTS
request_lookup = ProductSearch.RequestLookup(
    search_text = 'APPLE',
    limit = 10,
    offset = 0,
)
request_stock = ProductSearch.RequestStocks(
    indexId=5,
    isInUSGreenList=False,
    stockCountryId=886,
    offset=0,
    limit=100,
    requireTotal=True,
    sortColumns='name',
    sortTypes='asc',
)

# FETCH DATA
products_lookup = trading_api.product_search(request=request_lookup, raw=False)
stock_list = trading_api.product_search(request=request_stock, raw=False)

# LOOP OVER PRODUCTS
for product in stock_list.products:
    print(dict(product))

# LOOP OVER COLUMNS
product = stock_list.products[0]
for column in product:
    print(column, product[column])

# DISPLAY LOOKUP
for product in products_lookup.products:
    print(dict(product))