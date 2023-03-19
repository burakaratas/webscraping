

import requests
from bs4 import BeautifulSoup


gun = '04'
ay = '07'
yil = '2022'
saat = '1000'

myheader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


url = f'https://www.tcmb.gov.tr/reeskontkur/{yil}{ay}/{gun}{ay}{yil}-{saat}.xml'
response = requests.get(url, headers= myheader)

data = BeautifulSoup(response.content, 'xml')

dc = data.find_all('doviz_cinsi')
alis = data.find_all('alis')
birim = data.find_all('birim')

for i in range(0, len(dc)):
    print(dc[i].text, birim[i].text, alis[i].text)



"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi/Merkez+Bankasi+Faiz+Oranlari/faiz-oranlari'

response = requests.get(url)

data = BeautifulSoup(response.content, 'html.parser')

table = data.find(id='table table-striped')

rows = table.find_all('tr')


data = []
for row in rows:
    cols = row.find_all('td')
    cols = [item.text for item in cols]
    data.append(cols)

df = pd.DataFrame(data)
"""