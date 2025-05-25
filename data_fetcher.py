import requests
import pandas as pd

ALPHA_VANTAGE_API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol, interval="60min"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_VANTAGE_API_KEY,
        "datatype": "json"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data.get(f"Time Series ({interval})", {})
    df = pd.DataFrame.from_dict(time_series, orient='index').astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df
