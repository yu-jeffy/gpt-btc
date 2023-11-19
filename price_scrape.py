import requests
import json
from datetime import datetime

# Define the CoinGecko API URL for Bitcoin
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin"

# Define the function to get historical data
def get_historical_data(days):
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily'
    }
    response = requests.get(f"{COINGECKO_API_URL}/market_chart", params=params)
    return response.json()

# Fetch the data
today_data = requests.get(COINGECKO_API_URL).json()
daily_data_7d = get_historical_data(7)
three_months_data = get_historical_data(90)
six_months_data = get_historical_data(180)
one_year_data = get_historical_data(365)
two_year_data = get_historical_data(730)

# Combine all data into a single dictionary
all_data = {
    'today': today_data,
    'daily_7d': daily_data_7d,
    'three_months': three_months_data,
    'six_months': six_months_data,
    'one_year': one_year_data,
    'two_years': two_year_data
}

# Format the data for GPT-4 analysis
formatted_data = json.dumps(all_data, indent=4)

# Create a timestamp for the filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"price_data_{timestamp}.json"

# Save the formatted data to a file in the /results folder
with open(f"./results/{filename}", 'w') as file:
    file.write(formatted_data)

print(f"Data saved to /results/{filename}")