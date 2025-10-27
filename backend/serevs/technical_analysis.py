import pandas_ta as ta

class TechnicalAnalysis:
    def __init__(self, ):
        pass

    def rsi(self, df):
        return df.ta.rsi(close='Close', length=14, append=True)

    def macd(self, df):
        return df.ta.macd(close='Close', fast=12, slow=26, signal=19, append=True)

    def bollinger_bands(self, df):
        return df.ta.bbands(close=df['Close'], append=True)
    
    def sma(self, df):
        return df.ta.sma(close='Close', length=5)

    def 