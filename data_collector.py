import pandas as pd
import datetime
from tvDatafeed import TvDatafeed, Interval
from discordwebhook import Discord
import statistics
import mplfinance as mpf
import matplotlib as mpl
import pathlib
import math
import os 
import time 
from pathlib import Path

tv = TvDatafeed(username="cs.benliu@gmail.com",password="tltShort!1")
screener_data = pd.read_csv(r"C:\Screener\tmp\screener_data.csv")
numTickers = len(screener_data)
for i in range(numTickers):

        if str(screener_data.iloc[i]['Exchange']) == "NYSE ARCA":
            screener_data.at[i, 'Exchange'] = "AMEX"
for i in range(numTickers):
    ticker = screener_data.iloc[i]['Ticker']
    exchange = screener_data.iloc[i]['Exchange']
    print(ticker + f" {i}")
    try:
        if(os.path.exists("C:/Screener/data_csvs/" + ticker + "_data.csv") == False):
            data_daily = tv.get_hist(ticker, exchange, n_bars=3500)
            data_daily.to_csv("C:/Screener/data_csvs/" + ticker + "_data.csv")


    except TimeoutError:
        print(ticker + " timed out")

