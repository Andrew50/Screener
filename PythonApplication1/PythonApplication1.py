
if(dolVol > 1000000 and volume > 150000 and currPrice > 2 and pmChange != 0 and math.isnan(pmChange) != True):
		
	zfilter = 3.2
	gapzfilter0 = 8
	gapzfilter1 = 4
	changezfilter = 4
			
	data_daily = tv.get_hist(tick, exchange, n_bars=70) # get 20 past daily candles
	print(data_daily.head(1))
	length = len(data_daily)
	prevClose = data_daily.iloc[length-1][4]
	pmPrice = prevClose + pmChange
	todayGapValue = round(((pmPrice/prevClose)-1), 2)
	todayChangeValue = data_daily.iloc[length-1][4]/data_daily.iloc[length-1][1] - 1
			
	zdata = [] # 15 length
	zgaps = [] # 30 length=
	zchange = [] # 30 length
	for i in range(30):
		n = 29-i
		gapvalue = abs((data_daily.iloc[length-n][1]/data_daily.iloc[length-1-n][4]) - 1)
		changevalue = abs((data_daily.iloc[length-1-n][4]/data_daily.iloc[length-1-n][1]) - 1)
		datavalue = statistics.mean(data_daily.iloc[length-n-5:length-n-1][4])/data_daily.iloc[length-n][1]
	if i == 29:
		gapz1 = (gapvalue-statistics.mean(zgaps))/statistics.stdev(zgaps)
		zgaps.append(gapvalue)
		zchange.append(changevalue)
	if i > 14:
		zdata.append(datavalue)
				
				
				
	gapz = (todayGapValue-statistics.mean(zgaps))/statistics.stdev(zgaps)
	changez = (todayChangeValue - statistics.mean(zchange))/statistics.stdev(zchange) 
	value3 = (statistics.mean(data_daily.iloc[length-4:length][4]))/pmPrice
	z = (value3 - statistics.mean(zdata))/statistics.stdev(zdata) 
			
			
	print(f"z is = {z}, gapz is {gapz}")
	if (gapz1 < gapzfilter1 and gapz < gapzfilter0 and changez < changezfilter and z > zfilter and value3 > 0):
	z = round(z, 3)
	ourpath = pathlib.Path("D:/Screener/tvdatafeed/tmp") / "test.png"
	todayGapValuePercent = todayGapValue*100;
	mpf.plot(data_daily, type='candle', mav=(10, 20), volume=True, title=tick, hlines=dict(hlines=[pmPrice], linestyle="-."), style=s, savefig=ourpath)
	sendDiscordEmbed(tick + f" {prevClose} >> {pmPrice} ▲ {pmChange} ({todayGapValuePercent}%)", f"MR Setup, Z-Score: {z}")
	discord.post(file={"test": open("tmp/test.png", "rb")})