import yfinance as yf

tickers = ['AAPL', 'MSFT', 'MCD', ...]  # List of Dow Jones 30 tickers

def get_data(tickers):
    stock_data = {}
    for ticker in tickers:
        df = yf.download(ticker, start="2009-01-01", end="2020-05-08")
        stock_data[ticker] = df
    return stock_data

# Call the function to get the data
stock_data = get_data(tickers)
