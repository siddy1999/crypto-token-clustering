# src/data_loader.py
import os
import pandas as pd
import numpy as np

def load_token_log_returns(price_folder: str) -> pd.DataFrame:
    log_return_dict = {}

    for file in os.listdir(price_folder):
        if file.endswith(".csv"):
            token_name = file.replace(".csv", "")
            df = pd.read_csv(os.path.join(price_folder, file))

            df = df.rename(columns={"date": "Date", "price": "Close", "close": "Close"})
            df["Date"] = pd.to_datetime(df["Date"])
            df = df.sort_values("Date").set_index("Date")

            log_returns = np.log(df["Close"] / df["Close"].shift(1))
            log_returns.name = token_name
            log_return_dict[token_name] = log_returns

    combined = pd.concat(log_return_dict.values(), axis=1).dropna(how="all")
    return combined

def load_market_index(index_file: str) -> pd.Series:
    market_index = pd.read_csv(index_file, parse_dates=["Date"], index_col="Date")
    market_returns = np.log(market_index["Index_Level"] / market_index["Index_Level"].shift(1)).dropna()
    market_returns.name = "Market"
    return market_returns
