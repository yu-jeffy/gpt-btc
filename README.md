# gpt-btc

gpt-btc is a comprehensive Bitcoin analysis suite that utilizes GPT-4-1106 to provide insights into Bitcoin market trends, news sentiment, and blockchain data. The suite includes a Discord bot for real-time updates and a set of Python scripts for data scraping and analysis.

## About

gpt-btc leverages OpenAI's GPT-4-1106 model to analyze and summarize Bitcoin-related data. It scrapes price data from the CoinGecko API, fetches the 30 most recent BTC-related articles from the news API, and retrieves the latest block information, including halving estimates and hash rate calculations, from the block explorer API. Additionally, it provides a detailed summary of each news article and rates them for sentiment, relevance, and importance on a scale from 0 to 100, offering an objective metric and nuanced understanding of the current media landscape surrounding Bitcoin. This comprehensive suite provides a holistic view of the current state of Bitcoin, aiming to assist investors, researchers, and enthusiasts in making informed decisions by offering up-to-date and detailed analysis.

The Discord bot component allows users to receive daily Bitcoin analysis updates and manually trigger analysis on demand. The scraping scripts are designed to fetch the latest data from various sources, which is then processed and analyzed by the GPT-4 model.

## Set-Up

### Prerequisites
- Python 3.10.2 or higher
- An OpenAI API key for accessing GPT-4
- A Cryptonews API token for news scraping
- A Discord bot token and channel ID for the Discord bot
- The necessary Python packages installed

### Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/your-username/gpt-btc.git
   ```
2. Navigate to the cloned repository's directory:
   ```sh
   cd gpt-btc
   ```
3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory of the project and add your API keys and tokens:
   ```sh
   CRYPTONEWS_API_TOKEN=your_cryptonews_api_token
   OPENAI_API_KEY=your_openai_api_key
   DISCORD_TOKEN=your_discord_bot_token
   DISCORD_CHANNEL_ID=your_discord_channel_id
   ```
   Replace the placeholders with your actual keys and tokens.

## Usage

### Running the Discord Bot
1. Run the `gpt-btc_discord_bot.py` script:
   ```sh
   python gpt-btc_discord_bot.py
   ```
2. The bot will connect to your Discord server and start the scheduled analysis task.
3. Use the `!analyze` command in your Discord channel to manually trigger the Bitcoin analysis.

### Running the Analysis Scripts Manually
1. Run the `main.py` script to perform a full analysis:
   ```sh
   python main.py
   ```
2. The script will scrape the latest data, analyze it, and save the results to the `results` directory.

### Understanding the Output
- The output will include Bitcoin price trends, news sentiment analysis, and blockchain data insights.
- The Discord bot will post the analysis in the specified channel at the scheduled time or when manually triggered.

## Example Analysis Output

The example outputs provided below are derived from the three different data sources used by GPT-BTC: CoinGecko API for price data, the news API for recent BTC-related articles, and the block explorer API for the latest block information.

### Price Data Analysis (CoinGecko API)
- Date: 2023-04-01, Price (USD): 45000.00, Market Cap (USD): 850 billion, Volume (USD): 10 billion
- ...

### News Sentiment Analysis (News API)
- Title: Bitcoin Surges Amidst Economic Uncertainty
- Summary: The article discusses the recent surge in Bitcoin prices, attributing it to the growing economic uncertainty...
- Sentiment Rating: 85
- Market Relevance Rating: 90
- Importance Rating: 88
- ...

### Blockchain Data Insights (Block Explorer API)
- Current Block Height: 680000
- Estimated Halving Date: 2024-05-10
- Current Mining Difficulty: 14 trillion
- Estimated Network Hash Rate: 110 exahashes/second
- ...

### Final Consolidated Analysis
**Professional Market Report: Bitcoin Analysis**

**Executive Summary:**
This comprehensive report delves into the recent performance of Bitcoin (BTC), examining price movements, market capitalization, trading volume, and broader market trends. We analyze data from various dates and compare it to historical events, providing insights into potential future market behavior. The report also considers recent news and its impact on Bitcoin's market sentiment and potential price trajectory.

**Section 1: Price Data Analysis**
- **Price Fluctuations:** Bitcoin's price has exhibited volatility, with notable fluctuations between $26,000 and $38,000 over the analyzed period. The price peaked at $38,000 on November 16, 2023, followed by a decline to the $35,000 range, indicating resistance at higher levels.
- **Market Capitalization Trends:** Market capitalization has moved in tandem with price changes, reflecting investor sentiment and market liquidity. The highest market cap observed was $739 billion on November 16, 2023.
- **Volume Analysis:** Trading volume spiked on days with significant price movements, suggesting heightened market activity during periods of volatility. The highest volume recorded was $38 billion on November 16, 2023.

**Section 2: Market Trends and Sentiment**
- **Bull Rally Conclusion:** Recent data indicates the end of a bull rally, with a decrease in transaction volume and a shift in wallet holdings, particularly among wallets holding 10 – 10k BTC.
- **Investor Sentiment:** The fear and greed index points to 'greed,' which historically precedes market corrections. Technical indicators like bearish MACD crossover and RSI downtick support a potential bearish outlook.
- **Altcoin Impact:** Altcoins, including Ethereum, have followed Bitcoin's price trajectory, with a general market pullback observed. The performance of meme coins like Dogecoin and Shiba Inu also reflects a broader market sentiment shift.

**Section 3: Regulatory and Institutional Influence**
- **ETF Speculation:** Discussions around a U.S. SEC-approved spot Bitcoin ETF continue to influence market expectations. Analysts predict significant price surges if approved, with potential targets of $141,000 to $265,437 per BTC.
- **Institutional Interest:** Major financial firms, including Fidelity and BlackRock, are actively pursuing Bitcoin and Ethereum ETFs, indicating growing institutional interest and potential for increased market liquidity.

**Section 4: Technological and Ecosystem Developments**
- **Network Health:** Bitcoin's hashrate reached a seven-day high, though historically this has sometimes preceded price declines. The network's security remains robust, with mining difficulty and hashrate indicating strong computational power dedicated to transaction processing.
- **NFT Renaissance:** The resurgence of Bitcoin Ordinals and the rise in transaction fees due to NFT-like tokens on the Bitcoin network suggest a growing interest in Bitcoin's utility beyond a store of value.

**Section 5: Global Market Impact**
- **Geographical Factors:** South Korea's premium on Bitcoin prices and high trading volumes highlight regional market dynamics and the potential for arbitrage opportunities.
- **Cross-Border Payments:** Partnerships like Strike and Checkout.com aim to enhance Bitcoin's accessibility and use in international payments, potentially increasing adoption and demand.

**Section 6: Investment Considerations**
- **Long-Term Holding:** The increase in Bitcoin held by long-term investors signals confidence in the asset's future appreciation, despite short-term price volatility.
- **Market Entry Timing:** While the market presents opportunities above the $30,000 price level, investors must weigh the risks and conduct thorough research before making investment decisions.

**Conclusion:**
The current market analysis of Bitcoin reveals a complex interplay of investor sentiment, regulatory developments, technological advancements, and global market factors. While the end of the bull rally suggests a cautious approach, institutional interest and long-term holding trends provide a positive outlook for Bitcoin's future. Investors should remain vigilant, considering both the potential for growth and the inherent risks associated with cryptocurrency investments.

## Limitations and Considerations
- The accuracy of the analysis is dependent on the quality of the data scraped and the effectiveness of the GPT-4 model.
- The Discord bot requires the server to be running continuously for real-time updates.
- The analysis is based on available data and should not be the sole basis for investment decisions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
