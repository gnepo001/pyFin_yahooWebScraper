from requests import get as GET
from bs4 import BeautifulSoup as bs4

def getCompanyInfo(tickerlist):
    tickerPrice = []
    tickerBeta = []
    tickerPE = []
    tickerEPS = []
    tickerDiv = []
    pathString = "W(100%) M(0) Bdcl(c)"
    for ticker in tickerlist:    
        URL = "https://finance.yahoo.com/quote/{}?p={}".format(ticker,ticker)
        page = GET(URL)
        soup = bs4(page.content,"html.parser")
        #Price
        try:
            price = soup.find('span',{'class':"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
            tickerPrice.append(price)
        except:
            print("Error {}'s Price Could not be found!, None has been inserted!".format(ticker))
            tickerBeta.append(None)
        #beta
        try:
            beta = soup.find('table',{'class':pathString}).findAll('span')[3].text
            tickerBeta.append(beta)
        except:
            print("Error {}'s Beta Could not be found!, None has been inserted!".format(ticker))
            tickerBeta.append(None)
        #PE
        try:
            PE = soup.find('table',{'class':pathString}).findAll('span')[5].text
            tickerPE.append(PE)
        except:
            print("Error {}'s P/E Ratio Could not be found!, None has been inserted!".format(ticker))
            tickerPE.append(None)
        #EPS
        try:
            EPS = soup.find('table',{'class':pathString}).findAll('span')[7].text
            tickerEPS.append(EPS)
        except:
            print("Error {}'s EPS Ratio Could not be found!, None has been inserted!".format(ticker))
            tickerEPS.append(None)
        #Divdend
        try:
            PEratio = soup.find('table',{'class':pathString}).findAll('td')[11].text
            tickerDiv.append(PEratio)
        except:
            print("Error {}'s Divdend Ratio Could not be found!, None has been inserted!".format(ticker))
            tickerDiv.append(None)

    return  {tickerlist[i]:{"Price":tickerPrice[i],"Beta":tickerBeta[i],"PE":tickerPE[i],"EPS":tickerEPS[i],"Divident":tickerDiv[i]} for i in range(0,len(tickerlist))}

