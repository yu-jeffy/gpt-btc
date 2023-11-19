import os
import requests
import math
import time
from datetime import datetime

# Constants
HALVING_INTERVAL = 210000
SECONDS_PER_BLOCK = 600  # 10 minutes in seconds
RESULTS_DIR = "results"

# Function to fetch the latest block hash
def get_latest_block_hash():
    response = requests.get('https://blockchain.info/latestblock')
    response.raise_for_status()
    return response.json()['hash']

# Function to fetch block data using the block hash
def get_block_data(block_hash):
    response = requests.get(f'https://blockchain.info/rawblock/{block_hash}')
    response.raise_for_status()
    return response.json()

# Function to calculate the estimated time until the next Bitcoin halving
def estimate_halving_time(current_block_height):
    blocks_until_halving = HALVING_INTERVAL - (current_block_height % HALVING_INTERVAL)
    seconds_until_halving = blocks_until_halving * SECONDS_PER_BLOCK
    halving_timestamp = time.time() + seconds_until_halving
    return datetime.fromtimestamp(halving_timestamp)

# Function to calculate the current mining difficulty
def calculate_difficulty(bits):
    exponent = (bits >> 24) & 0xFF
    coeff = bits & 0xFFFFFF
    difficulty = 0x00FFFF / coeff * 2**(8*(exponent - 3))
    return difficulty

# Function to estimate the network hash rate based on the current difficulty
def estimate_network_hash_rate(difficulty):
    return difficulty * 2**32 / SECONDS_PER_BLOCK

# Function to write data to a text file with a timestamp in the results directory
def write_to_file(data):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{RESULTS_DIR}/bitcoin_data_{timestamp}.txt"
    with open(filename, 'w') as file:
        file.write(data)

# Main function to orchestrate the data retrieval and calculations
def main():
    try:
        # Fetch the latest block hash
        latest_block_hash = get_latest_block_hash()

        # Fetch the block data using the latest block hash
        block_data = get_block_data(latest_block_hash)
        current_block_height = block_data['height']
        bits = block_data['bits']

        # Calculate the estimated halving date
        halving_date = estimate_halving_time(current_block_height)

        # Calculate the current mining difficulty
        difficulty = calculate_difficulty(bits)

        # Estimate the network hash rate
        hash_rate = estimate_network_hash_rate(difficulty)

        # Prepare the data to be written to the file
        data = (
            f"Current Block Height: {current_block_height}\n"
            f"Estimated Halving Date: {halving_date}\n"
            f"Current Mining Difficulty: {difficulty}\n"
            f"Estimated Network Hash Rate: {hash_rate} hashes/second\n"
        )

        # Write the data to a file
        write_to_file(data)
        print("Data written to file successfully.")

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Run the main function
if __name__ == "__main__":
    main()
