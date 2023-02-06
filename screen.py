import os 
import time 
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from tvDatafeed import TvDatafeed, Interval
from discordwebhook import Discord
import statistics
import mplfinance as mpf
import matplotlib as mpl
import pathlib
import math

def sendDiscordMessage(msg): 
    discord.post(content=msg)

def sendDiscordEmbed(ticker, description):
    discord.post(
        embeds=[
        {

            "title": ticker,
            "description": description,
        }
        ],
    )
    
pc = 0
if pc == 0:
    pathf = "csben"
else: 
    pathf = ""


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
FireFoxDriverPath = os.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
FireFoxProfile = webdriver.FirefoxProfile()
FireFoxProfile.set_preference("General.useragent.override", user_agent)
browser = webdriver.Firefox(options=options, executable_path=FireFoxDriverPath)
browser.implicitly_wait(7)
browser.maximize_window()
discord = Discord(url="https://discord.com/api/webhooks/1071506429229416519/41ps0qlsiiFRDLxnZVCF5KuDtb_SWBHCwB5scK-YUf96mrBpzZRydsT2C4GiGPDAEmKW")
url = "https://www.tradingview.com/screener/"
browser.get(url)
mc = mpf.make_marketcolors(up='g',down='r')
s  = mpf.make_mpf_style(marketcolors=mc)
daysAgo = 50 # 0 is for the next session 
leftBuffer = 40

#START 
element_tab = browser.find_element(By.XPATH, '//div[@data-set="performance"]')
try:
    element_tab.click()
except ElementNotInteractableException:
    print('test')

time.sleep(0.5)

element_tab = browser.find_element(By.XPATH, '//div[@data-set="overview"]')
try:
    element_tab.click()
except ElementNotInteractableException:
    print('test')

#Logging into trading view
login_page = browser.find_element(By.XPATH, '//button[@aria-label="Open user menu"]')
login_page.click()
time.sleep(0.25)
login_page = browser.find_element(By.XPATH, '//button[@data-name="header-user-menu-sign-in"]')
login_page.click()
time.sleep(0.25)
login_page = browser.find_element(By.XPATH, '//span[@class="tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email"]')
login_page.click()
username = browser.find_element(By.XPATH, '//input[@name="username"]')
username.send_keys("cs.benliu@gmail.com")
time.sleep(0.5)
password = browser.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys("tltShort!1")
time.sleep(0.5)
login_button = browser.find_element(By.XPATH, '//button[@class="tv-button tv-button--size_large tv-button--primary tv-button--loader"]')
login_button.click()
time.sleep(1)
print(f'Scraping {url}...')
time.sleep(10)
print('wait over')



try:

    #setting default scanner settings
    browser.find_element(By.XPATH, '//div[@data-name="screener-field-sets"]').click()
    time.sleep(0.1)
    browser.find_element(By.XPATH, '//div[@data-set="overview"]').click()

    #seting filters
    filter_tab = browser.find_element(By.XPATH, '//div[@class="tv-screener-sticky-header-wrapper__fields-button-wrap"]')
    try:
        filter_tab.click()
    except ElementNotInteractableException:
        print('test')
    time.sleep(0.5)
    #Setting up the TV screener parameters
    tab1 = browser.find_element(By.XPATH, '//label[@data-field="earnings_per_share_basic_ttm"]')
    tab2 = browser.find_element(By.XPATH, '//label[@data-field="number_of_employees"]')
    tab3 = browser.find_element(By.XPATH, '//label[@data-field="sector"]')
    tab4 = browser.find_element(By.XPATH, '//label[@data-field="Recommend.All"]')
    tab6 = browser.find_element(By.XPATH, '//label[@data-field="price_earnings_ttm"]')
    tab7 = browser.find_element(By.XPATH, '//label[@data-field="relative_volume_intraday.5"]')
    tab8 = browser.find_element(By.XPATH, '//label[@data-field="change.1"]')
    tab9 = browser.find_element(By.XPATH, '//label[@data-field="change.5"]')
    tab10 = browser.find_element(By.XPATH, '//label[@data-field="change_from_open"]')
    tab11 = browser.find_element(By.XPATH, '//label[@data-field="exchange"]')
    tab12 = browser.find_element(By.XPATH, '//label[@data-field="premarket_change_abs"]')
    tab1.click()
    tab2.click()
    tab3.click()
    tab4.click()
    tab6.click()
    tab7.click()
    tab8.click()
    tab9.click()
    tab10.click()
    tab11.click()
    tab12.click()

    time.sleep(0.5) 
    browser.find_element(By.XPATH, '//div[@data-name="screener-filter-sets"]').click()
    time.sleep(0.25)
    browser.find_element(By.XPATH, '//span[@class="js-filter-set-name"]').click()
    time.sleep(0.25)
    sortRVol = browser.find_element(By.XPATH, '//div[@data-field="relative_volume_intraday.5"]')
    sortRVol.click()

    #creating the csv file
    download_screener_data = browser.find_element(By.XPATH, '//div[@data-name="screener-export-data"]')
    download_screener_data.click()
    time.sleep(1.5)
    today = str(datetime.date.today())
    downloaded_file = r"C:\Downloads\america_" + today + ".csv"
    new_name = r"C:\Downloads\screener_data.csv"
    os.rename(downloaded_file, new_name)
    os.replace(r"C:\Downloads\screener_data.csv", r"C:\Screener\tmp\screener_data.csv")
    tv = TvDatafeed(username="password",password="password")
    screener_data = pd.read_csv(r"C:\Screener\tmp\screener_data.csv")
    time.sleep(0.1)

    numTickers = len(screener_data)
    #Changing ARCA into AMEX
    for i in range(numTickers):
        if str(screener_data.iloc[i]['Exchange']) == "NYSE ARCA":
            screener_data.at[i, 'Exchange'] = "AMEX"
        if screener_data.iloc[i]['Pre-market Change'] is None:
            screener_data.at[i, 'Pre-market Change'] = 0


    #Loop stocks in screen
    for i in range(numTickers):
        tick = str(screener_data.iloc[i]['Ticker'])
        exchange = str(screener_data.iloc[i]['Exchange'])
        pmChange = screener_data.iloc[i]['Pre-market Change']
        currPrice = screener_data.iloc[i]['Price']
        volume = screener_data.iloc[i]['Volume']
        dolVol = screener_data.iloc[i]['Volume*Price']
        # Gaps Check 
        print(tick + f" {i}")
        if(dolVol > 1000000 and volume>150000 and currPrice > 3):
            if(daysAgo == 0 and pmChange != 0 and math.isnan(pmChange) != True):
                data_daily = tv.get_hist(tick, exchange, n_bars=100) # get 20 past daily candles
                print(data_daily.head(1))
                length = len(data_daily)
                gaps = []
                pmPrice = data_daily.iloc[length-1][4] + pmChange
                prevClose = data_daily.iloc[length-1][4]
                todayGapValue = round(((pmPrice/prevClose)-1), 2)
                for j in range(20): 
                        gaps.append((data_daily.iloc[length-1-j][1]/data_daily.iloc[length-2-j][4])-1)

                z = (todayGapValue-statistics.mean(gaps))/statistics.stdev(gaps)

                if(z < -5):
                    z = round(z, 3)
                    ourpath = pathlib.Path("C:/Screener/tmp") / "test.png"
                    todayGapValuePercent = todayGapValue*100;
                    mpf.plot(data_daily, type='candle', mav=(10, 20), volume=True, title=tick, hlines=dict(hlines=[pmPrice], linestyle="-."), style=s, savefig=ourpath)
                    sendDiscordEmbed(tick + f" {prevClose} >> {pmPrice} ▼ {pmChange} ({todayGapValuePercent}%)", f"NEP Setup, Z-Score: {z}")
                    discord.post(file={"test": open("tmp/test.png", "rb")})
                if(z > 5):
                    z = round(z, 3)
                    ourpath = pathlib.Path("C:/Screener/tmp") / "test.png"
                    todayGapValuePercent = todayGapValue*100;
                    mpf.plot(data_daily, type='candle', mav=(10, 20), volume=True, title=tick, hlines=dict(hlines=[pmPrice], linestyle="-."), style=s, savefig=ourpath)
                    sendDiscordEmbed(tick + f" {prevClose} >> {pmPrice} ▲ {pmChange} ({todayGapValuePercent}%)", f"EP Setup, Z-Score: {z}")
                    discord.post(file={"test": open("tmp/test.png", "rb")})
            else:
                try: 
                    data_daily = tv.get_hist(tick, exchange, n_bars=leftBuffer+daysAgo) # get daysAgo past daily candles + and extra hundred before that
                    keptRowNum = leftBuffer+51
                    data_daily = data_daily[:keptRowNum]
                    length = len(data_daily)
                    gaps = []
                    tdyOpen = data_daily.iloc[length-50][1]
                    prevClose = data_daily.iloc[length-51][4]
                    todayGapValue = round(((tdyOpen/prevClose)-1), 2)
                    datetimeOfDay = data_daily.index[length-50]
                    dateSplit = str(datetimeOfDay).split(" ")
                    date = dateSplit[0]
                    for j in range(20): 
                        gaps.append((data_daily.iloc[length-51-j][1]/data_daily.iloc[length-52-j][4])-1)
                    z = (todayGapValue-statistics.mean(gaps))/statistics.stdev(gaps)
                    if(z < -4):
                        z = round(z, 3)
                        ourpath = pathlib.Path("C:/Screener/tmp") / "test.png"
                        todayGapValuePercent = todayGapValue*100;
                        mpf.plot(data_daily, type='candle', mav=(10, 20), volume=True, vlines=dict(vlines=[date],linewidths=(1), alpha=0.25), title=tick, style=s, savefig=ourpath)
                        sendDiscordEmbed(tick, f"NEP Setup, Date: {date}, Z-Score: {z}")
                        discord.post(file={"test": open("tmp/test.png", "rb")})
                    if(z > 4):
                        z = round(z, 3)
                        ourpath = pathlib.Path("C:/Screener/tmp") / "test.png"
                        todayGapValuePercent = todayGapValue*100;
                        mpf.plot(data_daily, type='candle', mav=(10, 20), volume=True, vlines=dict(vlines=[date],linewidths=(1), alpha=0.25), title=tick, style=s, savefig=ourpath)
                        sendDiscordEmbed(tick, f"EP Setup, Date: {date}, Z-Score: {z}")
                        discord.post(file={"test": open("tmp/test.png", "rb")})  
                except IndexError:
                    pass
                except TimeoutError:
                    print("Timeout caught")
        # MR Check         
        if(dolVol > 1000000 and volume > 150000 and currPrice > 2 and pmChange != 0 and math.isnan(pmChange) != True):
            zfilter = 3.2
            gapzfilter0 = 8
            gapzfilter1 = 4
            changezfilter = 4
			
            data_daily = tv.get_hist(tick, exchange, n_bars=70) # get 20 past daily candles
            print(data_daily.head(1))
            length = len(data_daily) - 1
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
                lastCloses = 0
                for c in range(4): 
                    
                    lastCloses = lastCloses + data_daily.iloc[length-1-c-n][4]
                fourSMA = round((lastCloses/4), 2)
                datavalue = (fourSMA/data_daily.iloc[length-n][1] - 1)
                if i == 29:
                    gapz1 = (gapvalue-statistics.mean(zgaps))/statistics.stdev(zgaps)
                zgaps.append(gapvalue)
                zchange.append(changevalue)
                if i > 14:
                    zdata.append(datavalue)
				
				
				
            gapz = (todayGapValue-statistics.mean(zgaps))/statistics.stdev(zgaps)
            changez = (todayChangeValue - statistics.mean(zchange))/statistics.stdev(zchange) 
            lastCloses = 0
            for c in range(4): 
                    
                lastCloses = lastCloses + data_daily.iloc[length-c-n][4]
            fourSMA = round((lastCloses/4), 2)
            value3 = (fourSMA)/pmPrice
            z = (value3 - statistics.mean(zdata))/statistics.stdev(zdata) 
			
			
            print(f"z is = {z}, gapz is {gapz}")
            if (gapz1 < gapzfilter1 and gapz < gapzfilter0 and changez < changezfilter and z > zfilter and value3 > 0):
                z = round(z, 3)
                ourpath = pathlib.Path("C:/Screener/tmp") / "test.png"
                todayGapValuePercent = todayGapValue*100;
                mpf.plot(data_daily, type='candle', mav=(10, 20), volume=True, title=tick, hlines=dict(hlines=[pmPrice], linestyle="-."), style=s, savefig=ourpath)
                sendDiscordEmbed(tick + f" {prevClose} >> {pmPrice} ▲ {pmChange} ({todayGapValuePercent}%)", f"MR Setup, Z-Score: {z}")
                discord.post(file={"test": open("tmp/test.png", "rb")})
     



except (NoSuchElementException, TimeoutException):
    print("category not found")

