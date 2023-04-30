#!/usr/bin/env python3
"""
    Python porting of Bollinger Bands TradingView Indicator
    Developed by @edyatl <edyatl@yandex.ru> April 2023
    https://github.com/edyatl

"""
# Standard imports
import pandas as pd
import numpy as np
import talib as tl
import os
from os import environ as env
from dotenv import load_dotenv
from binance import Client

# Load API keys from env
project_dotenv = os.path.join(os.path.abspath(""), ".env")
if os.path.exists(project_dotenv):
    load_dotenv(project_dotenv)

api_key, api_secret = env.get("ENV_API_KEY"), env.get("ENV_SECRET_KEY")

# Make API Client instance
client = Client(api_key, api_secret)

short_col_names = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "qav",
    "num_trades",
    "taker_base_vol",
    "taker_quote_vol",
    "ignore",
]

# Load Dataset
# Get last 500 records of ATOMUSDT 15m Timeframe
klines = client.get_klines(symbol="ATOMUSDT", interval=Client.KLINE_INTERVAL_15MINUTE)
data = pd.DataFrame(klines, columns=short_col_names)

# Convert Open and Close time fields to DateTime
data["open_time"] = pd.to_datetime(data["open_time"], unit="ms")
data["close_time"] = pd.to_datetime(data["close_time"], unit="ms")

#--------------------------INPUTS--------------------------------
length: int = 20  # input.int(20, minval=1)
src: pd.Series = data["close"]  # input(close, title="Source")
mult: float = 2.0  # input.float(2.0, minval=0.001, maxval=50, title="StdDev")
# offset: int = 0  # input.int(0, "Offset", minval = -500, maxval = 500)

#--------------------------FUNCIONS------------------------------


def main():
    basis = tl.SMA(src, length)
    dev = mult * tl.STDDEV(src, length)

    upper = basis + dev
    lower = basis - dev

    res = pd.DataFrame(
        {
            "open_time": data["open_time"],
            "Basis": basis,
            "Deviation": dev,
            "Upper": upper,
            "Lower": lower,
        }
    )
    res.to_csv('bollinger-ATOMUSDT-15m.csv', index = None, header=True)


if __name__ == "__main__":
    main()
