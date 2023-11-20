import os
import re
import subprocess
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
    # Update the regex pattern to match the full timestamp with hyphens and underscores
    pattern = rf"{prefix}_\d{{4}}-\d{{2}}-\d{{2}}_\d{{2}}-\d{{2}}-\d{{2}}"
    files = [f for f in os.listdir(RESULTS_DIR) if re.match(pattern, f)]
    # Extract the timestamp from the filename and parse it with the correct format
    latest_file = max(files, key=lambda x: datetime.strptime(x[len(prefix) + 1:x.find('.txt')], '%Y-%m-%d_%H-%M-%S'))
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
    analysis_prompt = "Please analyze the following Bitcoin data in comprehensive detail and with granularity in detail. Provide a full professional market report, with financial and investing analysis, broken into sections, organized best depending on the analysis. This response must be 4000 tokens in length. Be direct, straightforward.:\n"+ concatenated_data
    
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
    
    # Write the response content to a file
    with open(filepath, 'w') as file:
        # Extract the content from the response
        content = response.choices[0].message.content
        file.write(content)

    # Print the content of the response and the path to the new file
    print(content)
    print(f"Analysis saved to: {filepath}")

# Run the main analysis function
if __name__ == '__main__':
    run_analysis()