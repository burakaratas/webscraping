
import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import pandas as pd
import numpy as np
import time
import ast
import json

# start_time = time.ctime()
# print(f"Start: {start_time}")


start_date = '01-01-1999'
end_date = '11-03-2023'
stock = 'EREGL'

b = Browser()
b.set_handle_robots(False)
b.addheaders = [('Referer', 'https://www.isyatirim.com.tr'), ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41')]

#https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?sektor=0001#page-4

URL = "https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?hisse=" + stock + "&startdate=" + start_date + "&enddate=" + end_date
URLtogo = URL
b.open(URLtogo)
soup = BeautifulSoup(b.response().read(), 'html.parser')
table = json.loads(str(soup))
table = table['value']
table = pd.DataFrame(table)
#print(table[['HGDG_HS_KODU','HGDG_TARIH','HGDG_KAPANIS','PD']])
#print(table[['HGDG_HS_KODU','HGDG_TARIH','HGDG_KAPANIS','PD','PD_USD']])


timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "webscraping\isyatirim-" + stock + timestr + ".csv"
table[['HGDG_HS_KODU','HGDG_TARIH','HGDG_KAPANIS','PD','PD_USD']].to_csv(filename, encoding="cp1254", errors="ignore")
