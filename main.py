import yfinance as yf
from time import sleep

def conditions(last_close, SMA20, SMA200, last_change):
    if last_close < SMA20 and last_close < SMA200:
         print("Trend =  Bearish")

    elif last_close > SMA20 and last_close > SMA200:
        print("Trend =Bullish")

    else:
        print('Trend = Neutral')
    
def SMA20s(closing_prices):
    return closing_prices.tail(20).mean(axis= 'index')


def SMA200s(closing_prices):
    return closing_prices.tail(200).mean(axis = 'index')


tickers = ['AAPL','BABA']
while True:
    for ticker in tickers:
        Prices = yf.download(ticker, period='2d', interval='2m')

        ClosingValues = Prices['Close']

        Percentage_change = ClosingValues.pct_change()

        last_close = ClosingValues.iloc[-1]

        last_change=Percentage_change.last('2m').iloc[-1]

        SMA20, SMA200 = SMA20s(ClosingValues), SMA200s(ClosingValues)

        print(ticker,"Price=",last_close)

        print("Percentage Change =", last_change)

        print('SMA20=',SMA20,'SMA200=',SMA200)

        conditions(last_close, SMA20, SMA200, last_change)
       

    sleep(120)