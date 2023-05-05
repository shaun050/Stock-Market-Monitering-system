import requests
import json

# Replace YOUR_API_KEY with your actual Alpha Vantage API key
api_key = 'LEDOEFY0L5JHXGOA'

# Specify the URL for the Alpha Vantage API
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=LEDOEFY0L5JHXGOA'

# Specify the parameters for the API request
params = {
    'function': 'LISTING_STATUS',
    'apikey': api_key,
}

# Send the API request and retrieve the response
response = requests.get(url, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Extract the list of symbols from the response
symbols = data['data']

# Print the list of symbols
print(symbols)
