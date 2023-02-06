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


def sendDiscordEmbedGainers(ticker, description):
    discordtopGainers.post(
        embeds=[
        {

            "title": ticker,
            "description": description,
        }
        ],
    )
def sendDiscordEmbedIntraday(ticker, description):
    discordintraday.post(
        embeds=[
        {

            "title": ticker,
            "description": description,
        }
        ],
    )
user = 'cs.benliu@gmail.com'
password = 'tltShort!1'
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
FireFoxDriverPath = os.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
FireFoxProfile = webdriver.FirefoxProfile()
FireFoxProfile.set_preference("General.useragent.override", user_agent)
browser = webdriver.Firefox(options=options, executable_path=FireFoxDriverPath)
browser.implicitly_wait(7)
browser.maximize_window()
discordtopGainers = Discord(url="https://discord.com/api/webhooks/1071666210514669648/dSLYGAB5CWQuulV46ePmExwgljauPexCG10R2ZqZctTl7lyya-Zs7lJ7ecLjQEruAfYw")
discordintraday = Discord(url="https://discord.com/api/webhooks/1071667193709858847/qwHcqShmotkEPkml8BSMTTnSp38xL1-bw9ESFRhBe5jPB9o5wcE9oikfAbt-EKEt7d3c")
url = "https://www.tradingview.com/screener/"
browser.get(url)
mc = mpf.make_marketcolors(up='g',down='r')
s  = mpf.make_mpf_style(marketcolors=mc)
time.sleep(2)
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
    tab13 = browser.find_element(By.XPATH, '//label[@data-field="open"]')
    tab14 = browser.find_element(By.XPATH, '//label[@data-field="change_from_open_abs"]')
    tab15 = browser.find_element(By.XPATH, '//label[@data-field="change_from_open"]')
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
    tab13.click()
    tab14.click()
    tab15.click()
    time.sleep(0.5) 
    browser.find_element(By.XPATH, '//div[@data-name="screener-filter-sets"]').click()
    time.sleep(0.25)
    browser.find_element(By.XPATH, '//span[@class="js-filter-set-name"]').click()
    time.sleep(0.25)
    sortRVol = browser.find_element(By.XPATH, '//div[@data-field="change.1"]')
    sortRVol.click()
    count = 0
    tv = TvDatafeed(username=user,password=password)
    listTickersBurst = []
    listTickersGainers = []
    counter = 0
    while(True):
        #creating the csv file
        browser.find_element(By.XPATH, '//div[@data-name="screener-refresh"]').click()
        browser.find_element(By.XPATH, '//div[@data-name="screener-refresh"]').click()
        download_screener_data = browser.find_element(By.XPATH, '//div[@data-name="screener-export-data"]')
        download_screener_data.click()
        time.sleep(2)
        today = str(datetime.date.today())
        downloaded_file = r"C:\Downloads\america_" + today + ".csv"
        new_name = r"C:\Downloads\screener_data_intraday.csv"
        os.rename(downloaded_file, new_name)
        os.replace(r"C:\Downloads\screener_data_intraday.csv", r"C:\Screener\tmp\screener_data_intraday.csv")
        screener_data = pd.read_csv(r"C:\Screener\tmp\screener_data_intraday.csv")
        time.sleep(0.1)

        numTickers = len(screener_data)
        #Changing ARCA into AMEX
        for i in range(numTickers):
            if str(screener_data.iloc[i]['Exchange']) == "NYSE ARCA":
                screener_data.at[i, 'Exchange'] = "AMEX"

        #Loop stocks in screen
        for i in range(numTickers):
            tick = str(screener_data.iloc[i]['Ticker'])
            exchange = str(screener_data.iloc[i]['Exchange'])
            change = round(screener_data.iloc[i]["Change 1m, %"], 2)
            dayChange = round(screener_data.iloc[i]['Change %'], 2)
            changeFromOpen = screener_data.iloc[i]['Change from Open']
            openValue = screener_data.iloc[i]['Open']
            currPrice = screener_data.iloc[i]['Price']
            volume = screener_data.iloc[i]['Volume']

            if(change > 2.5 and volume > 250000 and volume*currPrice > 750000 and currPrice > 1.2):
                data_minute_100 = tv.get_hist(tick, exchange, interval=Interval.in_1_minute, n_bars=100)
                print(data_minute_100.head(1))
                ourpath = pathlib.Path("C:/Screener/tmp") / "test3.png"
                openCandlePrice = float(data_minute_100.iloc[len(data_minute_100)-1][1])
                changePrice = round(float(currPrice - openCandlePrice), 2)
                marketCap = float(screener_data.iloc[i]['Market Capitalization'])
                marketCapText = round((marketCap / 1000000000), 2)
                relativeVolAtTime = round(screener_data.iloc[i]['Relative Volume at Time'], 1)
                mpf.plot(data_minute_100, type='candle', volume=True, title=tick, style=s, savefig=ourpath)
                sendDiscordEmbedIntraday(tick + f" {openCandlePrice} >> Current: {currPrice} ▲ {changePrice} ({change}%)", f"Intraday % Gaining Setup, Volume: {volume}, RelVol: {relativeVolAtTime}x, MCap: ${marketCapText}B")
                discordintraday.post(file={"test": open("tmp/test3.png", "rb")})
            if(dayChange > 15 and volume > 500000 and volume*currPrice > 7500000 and currPrice > 1.2 and (counter % 5 == 0)): 
                data_minute_100 = tv.get_hist(tick, exchange, interval=Interval.in_1_minute, n_bars=250)
                print(data_minute_100.head(1))
                ourpath = pathlib.Path("C:/Screener/tmp") / "test3.png"
                
                marketCap = float(screener_data.iloc[i]['Market Capitalization'])
                marketCapText = round((marketCap / 1000000000), 2)
                relativeVolAtTime = round(screener_data.iloc[i]['Relative Volume at Time'], 1)
                mpf.plot(data_minute_100, type='candle', volume=True, title=tick, style=s, savefig=ourpath)
                sendDiscordEmbedGainers(tick + f" {openValue} >> {currPrice} ▲ {changeFromOpen} ({dayChange}%)", f"Top Gainer, Volume: {volume}, RelVol: {relativeVolAtTime}x, MCap: ${marketCapText}B")
                discordtopGainers.post(file={"test": open("tmp/test3.png", "rb")})
            
        time.sleep(60)
        sendDiscordEmbedGainers("NEW BATCH !", "Time: " + str(datetime.datetime.now()))
        counter = counter + 1



except (NoSuchElementException, TimeoutException):
    print("category not found")


