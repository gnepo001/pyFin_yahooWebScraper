import yahooWebScraper   
import time
import pandas as pd

t = time.time()
stocks = ["AAPL","AMZN","AMD","TSLA",'SPY']

x = pd.DataFrame.from_dict(yahooWebScraper.getCompanyInfo(stocks))

print(x)

print("Time Taken to collect: "+str(time.time()-t)+" seconds")