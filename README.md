#Yahoo simple summary webscraper
-returns a dictionary of the given tickers
-Dictionary is used to easily convert to a pandas dataframe
-test.py is included for testing purpose (run to make sure it work :))
Note: tickers must be valid on yahoo

#Example
import yahooWebScraper   
import pandas as pd

stocks = ["AAPL","AMZN","AMD","TSLA",'SPY']

x = pd.DataFrame.from_dict(yahooWebScraper.getCompanyInfo(stocks))

print(x)