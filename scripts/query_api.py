# Import API key data for user from config.py file
import config

import requests

"""
This script uses Alpha Vantage, which limits API calls to:
5 API requests per minute; 500 API requests per day

Example API request to Alpha Vantage:
https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo

See more options for API calls on the Alpha Vantage documentation page:
https://www.alphavantage.co/documentation/#
"""

### NOTE - NEED TO ADD CHECK FOR VALID TICKER SYMBOLS ###

def make_query(function, symbol, *args):
    # build query function here
    function = function
    symbol = symbol
    apikey = config.api_key
    response = requests.get("https://www.alphavantage.co/query" +
                           "?function=" + function +
                           "&symbol=" + symbol +
                           "&apikey=" + apikey)
    
    data = response.json()

    for i in data:
        print(i + ":", data[i])
    print('\n')

# Gets input from user
ticker = input("Enter ticker symbol, or 'wlist' to use watchlist\n")

if ticker == 'wlist':
    import watchlist
    for i in watchlist.ticks:
        make_query('OVERVIEW', i)

else:
    make_query('OVERVIEW', ticker)
