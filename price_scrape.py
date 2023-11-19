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

# Function to clean and summarize the data for GPT-4 analysis
def clean_and_summarize_data(historical_data):
    # Extract date, price, market cap, and volume from the historical data
    prices = historical_data['prices']
    market_caps = historical_data['market_caps']
    total_volumes = historical_data['total_volumes']
    
    # Create a summary string
    summary = "Date, Price (USD), Market Cap (USD), Volume (USD)\n"
    for price, market_cap, total_volume in zip(prices, market_caps, total_volumes):
        date = datetime.utcfromtimestamp(price[0] / 1000).strftime('%Y-%m-%d')
        price_usd = price[1]
        market_cap_usd = market_cap[1]
        volume_usd = total_volume[1]
        summary += f"{date}, {price_usd:.2f}, {market_cap_usd:.2f}, {volume_usd:.2f}\n"
    return summary

# Fetch the data
today_data = requests.get(COINGECKO_API_URL).json()
daily_data_7d = get_historical_data(7)
three_months_data = get_historical_data(90)
six_months_data = get_historical_data(180)
one_year_data = get_historical_data(365)
two_year_data = get_historical_data(730)

# Clean and summarize the data
summary_7d = clean_and_summarize_data(daily_data_7d)
summary_3m = clean_and_summarize_data(three_months_data)
summary_6m = clean_and_summarize_data(six_months_data)
summary_1y = clean_and_summarize_data(one_year_data)
summary_2y = clean_and_summarize_data(two_year_data)

# Combine all summaries
all_summaries = "\n".join([summary_7d, summary_3m, summary_6m, summary_1y, summary_2y])

# Create a timestamp for the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"price_data_{timestamp}.txt"

# Save the summarized data to a file in the /results folder
with open(f"./results/{filename}", 'w') as file:
    file.write(all_summaries)

print(f"Data saved to /results/{filename}")