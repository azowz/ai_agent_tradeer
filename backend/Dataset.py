import yfinance as yf


class GetData:
    def __init__(self):
        pass

    def download_data(self, company_name, time_period='1y'):
        ticker = yf.Ticker(company_name)
        hist = ticker.history(period=time_period)
        hist = hist[['Open', 'High', 'Low', 'Close', 'Volume']]
        return hist

    def store_into_database(self):
        pass

    def get_data_from_database(self):
        pass

    def get_all_company_tickers(self):

        return ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'GOOGL', 'NVDA',
                'TSLA', 'META', 'BRK-B', 'JPM', 'V', 'UNH', 'HD',
                'PG', 'MA', 'INTC', 'ORCL', 'KO', 'PFE', 'DIS']

