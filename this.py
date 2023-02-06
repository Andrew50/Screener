from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import datetime
import statistics

#data = tv.get_hist('BTCUSD', 'BINANCE', interval=Interval.in_1_minute)
tv = TvDatafeed(username="44cs.benliu@gmail.com",password="tltShor!1")
tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA', 'NVDA', 'META', 'ASML',
     'CSCO', 'ADBE', 'COST', 'GEN', 'AZN', 'TXN', 'AMD']
for tick in tickers: 
    data_daily = tv.get_hist(tick, 'NASDAQ', n_bars=70) #get the most recent candle of pre market
    cs = pd.read_csv(f"D:/Screener/scanner/data_csvs/CLFD_data.csv")
    print(type(cs.index[50]))
    print(cs.index[50])
    #test = data_daily.loc[dt]
    #print(data_daily.tail())
    #length = len(data_daily)
    #print(data_daily.index[5])
    #print(type(data_daily.index[5]))



    #todayGapValue = (data_minute.iloc[0][4]/data_daily.iloc[length-1][4])-1
    #print(data_daily.tail())
    #for i in range(length): 
    #    if i > 0:
    #        gaps.append((data_daily.iloc[i][2]/data_daily.iloc[i-1][4])-1)

    #z = (todayGapValue-statistics.mean(gaps))/statistics.stdev(gaps)
    #if(z < -2):
    #    print(str(tick))





