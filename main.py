import yfinance as yf
from time import sleep

def SMA20s(closing_prices):
    return closing_prices.tail(20).mean(axis= 'index')


def SMA200s(closing_prices):
    return closing_prices.tail(200).mean(axis = 'index')

def change():
    Percentage_change = ClosingValues.pct_change()
    last_change = Percentage_change.iloc[-1]
    return last_change

def buy():
    above_fat = {ticker: changed}
    buy_signal.update(above_fat)
    buy_signal.update()

def sell():
    below_fat = {ticker: changed}
    buy_signal.update(below_fat)

def neutral():
    between_fat = {ticker: changed}
    neutral_signal.update(between_fat)

tickers = ['PTON','AAPL','BABA','PDD','NKE','SBUX','FSLY','FB','MSFT','MU','TWTR','QCOM','UAL','JD']

while True:

        buy_signal={}
        sell_signal={}
        neutral_signal={}

        for ticker in tickers:


            #last Close Value
            Prices = yf.download(ticker, period='2d', interval='2m')
            ClosingValues = Prices['Close']
            last_close = ClosingValues.iloc[-1]


            # Percentage Change
            changed = change()



            # SMA20/SMA200
            SMA20, SMA200 = SMA20s(ClosingValues), SMA200s(ClosingValues)

            buy_condition=[
                last_close>SMA20,
                last_close>SMA200,
                   ]
            sell_condition = [
                last_close < SMA200,
                last_close < SMA20
            ]
            if all(buy_condition):
                buy()
            elif all(sell_condition):
                sell()
            else:
                neutral()



        # Sorting Process
        sorted_buy = dict(sorted(buy_signal.items(), key=lambda x: x[0], reverse=True))
        sorted_sell=dict(sorted(sell_signal.items(),key=lambda x: x[0]))

        # Finalizing Values
        print("Above Fat4:",sorted_buy,"\n\n\n")
        print("Below Fat4:",sorted_sell,"\n\n\n")
        print("Between SMA20 and SMA200:",neutral_signal,"\n\n\n")

           
        sleep(120)
