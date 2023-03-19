
#Hepsiemlak
#KİRALIK/SATILIK

import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import time

start_time = time.ctime()
print(f"Start: {start_time}")

kiralik_satilik_flag = 1
# kiraliksa 0, satiliksa 1

if (kiralik_satilik_flag == 0):
    tip = "kiralik"
else:
    tip = "satilik"

b = Browser()
b.set_handle_robots(False)
b.addheaders = [('Referer', 'https://www.hepsiemlak.com'), ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41')]

URL = "https://www.hepsiemlak.com/istanbul-" + tip +"-3-1?counties=atasehir,cekmekoy,kadikoy,kartal,maltepe,pendik,sancaktepe,sultanbeyli,tuzla,umraniye,uskudar&sortField=PRICE&sortDirection=DESC"
URLtogo = URL
b.open(URLtogo)
soup = BeautifulSoup(b.response().read(), 'html.parser')

pages = soup.find_all('li',{'class':'he-pagination__item'})
page_list = [page.get_text().strip() for page in pages]
nr_pages = int(page_list[-1])-1
print(f'Toplam: {nr_pages}')
# 298 sayfa 17 dk.

id_all = []
title_all = []
price_all = []
m2_all = []
#room_all = []
loc_all = []
date_all = []
age_all = []
floor_all = []


for i in range(0,nr_pages):

    print(f"{i+1}.sayfa")
    URL = "https://www.hepsiemlak.com/istanbul-" + tip +"-3-1?counties=atasehir,cekmekoy,kadikoy,kartal,maltepe,pendik,sancaktepe,sultanbeyli,tuzla,umraniye,uskudar&sortField=PRICE&sortDirection=DESC&page=" + str(i+1)
    URLtogo = URL
    b.open(URLtogo)
    soup = BeautifulSoup(b.response().read(), 'html.parser')

    ids = soup.find_all('span',{'class':'phone-listing-id'})
    id_list = [id.get_text().strip().replace("İlan No: ","") for id in ids]
    id_all.extend(id_list)

    prices = soup.find_all('span',{'class':'list-view-price'})
    price_list = [price.get_text().strip().replace("\n","").replace(" ","").replace("TL","") for price in prices]
    price_all.extend(price_list)

    dates = soup.find_all('span',{'class':'list-view-date'})
    date_list = [date.get_text().strip() for date in dates]
    date_all.extend(date_list)

    # rooms = soup.find_all('span',{'class':'celly houseRoomCount'})
    # room_list = [room.get_text().strip() for room in rooms]
    # print(room_list)  

    m2s = soup.find_all('span',{'class':'celly squareMeter list-view-size'})
    m2_list = [m2.get_text().strip().replace(" m2","") for m2 in m2s]
    m2_all.extend(m2_list)

    ages = soup.find_all('span',{'class':'celly buildingAge'})
    age_list = [age.get_text().strip().replace("Sıfır Bina","0") for age in ages]
    age_all.extend(age_list)

    floors = soup.find_all('span',{'class':'celly floortype'})
    floor_list = [floor.get_text().strip() for floor in floors]
    floor_all.extend(floor_list)

    titles = soup.find_all('header',{'class':'list-view-header'})
    title_list = [title.get_text().strip() for title in titles]
    title_all.extend(title_list)

    locs = soup.find_all('div',{'class':'list-view-location'})
    loc_list = [loc.get_text().strip().replace("\n","").replace("  ","") for loc in locs]
    loc_all.extend(loc_list)


import pandas as pd
entry_dict = {'ID': id_all, 'Title': title_all, 'Price': price_all, 'M2': m2_all, 'Location': loc_all, 'Date': date_all, 'Age':age_all, 'Floor':floor_all, }
entry_dict_df = pd.DataFrame(entry_dict)
print(entry_dict_df)

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "webscraping\hepsiemlak" + tip + timestr + ".csv"
entry_dict_df.to_csv(filename, encoding="cp1254", errors="ignore")

end_time = time.ctime()
print(f"End: {end_time}")
