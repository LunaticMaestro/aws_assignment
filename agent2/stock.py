import yfinance as yf
import pandas as pd
import json

def get_3m_data(ticker):
    # Get the ticker data for the last 3 months
    stock_data = yf.Ticker(ticker)
    # Fetch the historical data for the past 3 months
    df = stock_data.history(period='3mo')
    return df

def to_json(df, ticker):
    # Convert DataFrame to JSON and return it wrapped in a dictionary
    json_data = df.to_json(orient='records', date_format='iso')
    response = {ticker: json_data}
    return response

if __name__ == "__main__":
    # Example usage
    ticker = 'AAPL'
    df = get_3m_data(ticker)
    json_response = to_json(df, ticker)
    print(json_response)
