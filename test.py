import yahooWebScraper   
import time
import pandas as pd

t = time.time()
stocks = ["AAPL","AMZN","MSFT","FB","T","LULU","AMD","TSLA",'SPY']

x = pd.DataFrame.from_dict(yahooWebScraper.getCompanyInfo(stocks),orient='index')

print(x)

print("Time Taken to collect: "+str(time.time()-t)+" seconds")