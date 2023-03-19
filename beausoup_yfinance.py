
import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import time
import pandas as pd
import numpy as np


b = Browser()
b.set_handle_robots(False)
b.addheaders = [('Referer', 'https://finance.yahoo.com'), ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41')]

bank_list = np.loadtxt("webscraping\mybanklist.csv", skiprows = 1, dtype = "str")
#bank_list = ['BBVA','JPM']
nrbanks = len(bank_list)

value_all = []

URL = "https://finance.yahoo.com/quote/BBVA/key-statistics?p=BBVA"
URLtogo = URL
b.open(URLtogo)
soup = BeautifulSoup(b.response().read(), 'html.parser')
col_data = soup.find_all('td',{'class': lambda L: L and L.startswith('Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px)') })
column_list = [element.get_text().strip() for element in col_data]
column_list.insert(0,"Bank Name")


for i in bank_list:
    print(f'{i}')
    URL = "https://finance.yahoo.com/quote/"+i+"/key-statistics?p="+i
    URLtogo = URL
    b.open(URLtogo)
    soup = BeautifulSoup(b.response().read(), 'html.parser')

    values = soup.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})
    value_list = [value.get_text().strip() for value in values]
    value_list.insert(0,i)
    value_all.append(value_list)


datatable = pd.DataFrame(value_all, columns = column_list)
print(datatable)

filename = "webscraping\mybankdata.csv"
datatable.to_csv(filename, encoding="utf-8", errors="ignore")