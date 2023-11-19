import price_scrape
import news_scrape
import blockexplorer_scrape

import os
import re
import subprocess
from datetime import datetime

import openai

# Define the path to the results folder
RESULTS_DIR = './results'

# Define the system prompt
system_prompt = (
    "You are a Bitcoin specialist, investment manager, and financial analyzer. "
    "You provide professional, insightful, and reasoning-backed analysis of the market "
    "and trading opportunities."
)

# Function to run the scraping scripts
def run_scraping_scripts():
    subprocess.run(['python', 'price_scrape.py'])
    subprocess.run(['python', 'news_scrape.py'])
    subprocess.run(['python', 'blockexplorer_scrape.py'])

# Function to get the latest file with a specific prefix
def get_latest_file(prefix):
    files = [f for f in os.listdir(RESULTS_DIR) if re.match(rf'{prefix}_\d+', f)]
    latest_file = max(files, key=lambda x: datetime.strptime(x[len(prefix) + 1:x.find('.txt')], '%Y%m%d_%H%M%S'))
    return os.path.join(RESULTS_DIR, latest_file)

# Function to read and title the file contents
def read_and_title_file(filepath, title):
    with open(filepath, 'r') as file:
        content = file.read()
    return f"{title}:\n{content}\n"

# Main function to run the analysis
def run_analysis():
    # Run the scraping scripts
    run_scraping_scripts()
    
    # Get the latest files
    price_file = get_latest_file('price_data')
    news_file = get_latest_file('news_analysis')
    bitcoin_file = get_latest_file('bitcoin_data')
    
    # Read and concatenate the file contents with titles
    concatenated_data = (
        read_and_title_file(price_file, 'PRICE DATA') +
        read_and_title_file(news_file, 'NEWS ANALYSIS') +
        read_and_title_file(bitcoin_file, 'BLOCK EXPLORER DATA')
    )
    
    # Define the analysis prompt
    analysis_prompt = "Please analyze the following Bitcoin data:\n" + concatenated_data
    
    # Create the chat completion
    response = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": analysis_prompt}
        ],
        temperature=0.3,
        max_tokens=4000
    )
    
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"file_analysis_{timestamp}.txt"
    filepath = os.path.join(RESULTS_DIR, filename)
    
    # Write the response to a file
    with open(filepath, 'w') as file:
        file.write(str(response))

    # Print response and the path to the new file
    print(response)
    print(f"Analysis saved to: {filepath}")

# Run the main analysis function
if __name__ == '__main__':
    run_analysis()