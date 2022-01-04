import matplotlib.pyplot as plt
import pendulum
import yfinance as yf
from PIL import Image

def get_ticker(ticker):
    stock_info = yf.Ticker(ticker).info
    # stock_info.keys() for other properties you can explore
    market_price = stock_info['regularMarketPrice']
    previous_close_price = stock_info['regularMarketPreviousClose']
    print('market price ', market_price)
    print('previous close price ', previous_close_price)

    price_history = yf.Ticker(ticker).history(period='1d',  # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                              interval='1m',
                                              # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                              actions=False)
    time_series = list(price_history['Open'])
    dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]
    plt.style.use('dark_background')
    plt.plot(dt_list, time_series, linewidth=2)
    plt.show()


def main():
    get_ticker('TSLA')


if __name__ == '__main__':
    main()

