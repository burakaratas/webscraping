
#Fonlara Ait Bilgiler

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

URL = "https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="

fon_kodlari = ["AFA","AFV","AFS","AFT"]

mycolumns = ['Kodu', 'ISIN Kodu', 'Platform İşlem Durumu', 'İşlem Başlangıç Saati', 'Son İşlem Saati', 'Fon Alış Valörü', 'Fon Satış Valörü', 
'Min. Alış İşlem Miktarı', 'Min. Satış İşlem Miktarı', 'Max. Alış İşlem Miktarı', 'Max. Satış İşlem Miktarı', 'Giriş Komisyonu', 'Çıkış Komisyonu', 'Fonun Faiz İçeriği', 'Fonun Risk Değeri']


item_info_list_all = np.empty([0, 15])


for i in range(len(fon_kodlari)):
    URLtogo = URL+str(fon_kodlari[i])
    response = requests.get(URLtogo)
    soup = BeautifulSoup(response.content, 'html.parser')

    item_info = soup.find_all('td',{'class':'fund-profile-item'})
    item_info_list = [x.get_text().strip() for x in item_info]
    item_info_list_all = np.vstack([item_info_list_all,np.array([item_info_list])])


mydf = pd.DataFrame(item_info_list_all, columns= mycolumns)
print(mydf)