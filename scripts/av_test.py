# Import API key data for user from config.py file
import config
# Import watchlist from watchlist.py
import watchlist

import requests

"""
This script uses Alpha Vantage, which limits API calls to:
5 API requests per minute; 500 API requests per day

Example API request to Alpha Vantage:
https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo

See more options for API calls on the Alpha Vantage documentation page:
https://www.alphavantage.co/documentation/#
"""

function = 'OVERVIEW'
#symbol = 'FLIR'
apikey = config.api_key

for i in watchlist.ticks:
    symbol = i
    response = requests.get("https://www.alphavantage.co/query" + 
                            "?function=" + function + 
                            "&symbol=" + symbol + 
                            "&apikey=" + apikey)

    data = response.json()

    print('Symbol: ', data['Symbol'])
    print('PE Ratio: ', data['PERatio'], '\n')

