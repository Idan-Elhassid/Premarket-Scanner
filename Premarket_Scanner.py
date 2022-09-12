import pandas as pd
import requests

# creating the Dataframe from the marketwatch premarket volume site
tables = pd.read_html("https://www.marketwatch.com/tools/screener/premarket")
df_gainers = tables[0]
df_losers = tables[1]

biggest_winner = df_gainers.iloc[[0]]
biggest_loser = df_losers.iloc[[0]]


# to get a clean stock ticker these lines are needed
loser_ticker_string = str(biggest_loser['Symbol  Symbol'].values[0])
loser_ticker_split_for_cleaning = loser_ticker_string.split()
loser_ticker = (loser_ticker_split_for_cleaning[0])

winner_ticker_string = str(biggest_winner['Symbol  Symbol'].values[0])
winner_ticker_split_for_cleaning = winner_ticker_string.split()
winner_ticker = (winner_ticker_split_for_cleaning[0])

list_of_tickers = [winner_ticker, loser_ticker]

# here we will connect to alphavantage's API
for item in list_of_tickers:
    subject = f"check out {item}.\nnews links:"
    print(subject)
    # your API key goes in the next line...
    api_key = ""
    stock_endpoint = "https://www.alphavantage.co/query/"

    stock_params = {
        "function": "NEWS_SENTIMENT",
        "tickers": item,
        "apikey": api_key,

    }
    response = requests.get(stock_endpoint, params=stock_params)
    data = response.json()
    data_list = [value for (key, value) in data.items()]
    # we will get the top 3 news pieces for our stocks
    for number in range(0, 3):
        news_title = data_list[3][number]["title"]
        news_url = data_list[3][number]["url"]
        print(news_title, news_url)
    print("-------")
