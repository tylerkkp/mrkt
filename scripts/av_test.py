# Import API key data for user from config.py file
import config

import requests

# Example API request to Alpha Vantage:
# https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
function = 'OVERVIEW'
symbol = 'IBM'
apikey = config.api_key

response = requests.get("https://www.alphavantage.co/query" + 
                        "?function=" + function + 
                        "&symbol=" + symbol + 
                        "&apikey=" + apikey)

data = response.json()

print('Symbol: ', data['Symbol'])
print('PE Ratio: ', data['PERatio'])