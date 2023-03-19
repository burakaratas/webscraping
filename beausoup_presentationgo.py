
#Presentationgo

import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import time
import re


def download_url(url,name):
   file_name_start_pos = url.rfind("/") + 1
   file_name = "downloader/presentationgo/" + str(name) + ".pptx"

   r = requests.get(url, stream=True)
   if r.status_code == requests.codes.ok:
      with open(file_name, 'wb') as f:
        for data in r:
           f.write(data)


start_time = time.ctime()
print(f"Start: {start_time}")

b = Browser()
b.set_handle_robots(False)
b.addheaders = [('Referer', 'https://www.presentationgo.com'), ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41')]


links_all = []
dlinks_all = []
dlinks_all_name = []

#nr_pages = 93
start_page = 71
end_page = 80

for i in range(start_page,end_page+1):
    print(f"Sayfa: {i}")
    URL = "https://www.presentationgo.com/presentation/category/charts-diagrams/page/" + str(i) + "/"
    URLtogo = URL
    b.open(URLtogo)
    soup = BeautifulSoup(b.response().read(), 'html.parser')
    pages = soup.find_all('h2',{'class': 'gb-headline gb-headline-0c95003a gb-headline-text'})
    for page in pages:
        page = str(page)
        page = page[71:(page.find('/">'))]
        links_all.append(page)

for link in links_all:
    b.open(link)
    soupx = BeautifulSoup(b.response().read(), 'html.parser')
    s = soupx.find_all('a',{'class': 'button powerpoint'})
    x = str(s[1])
    x = x[35:(x.find('rel')-2)]
    dlinks_all.append(x)
    name = x[x.find('/download/')+10:x.find('/?')]
    dlinks_all_name.append(name)

i = len(dlinks_all)

for a in range(0,i):
    download_url(str(dlinks_all[a]),str(dlinks_all_name[a]))
    print(f"Downloaded: {dlinks_all_name[a]}")


import pandas as pd
template_list = {'Webpage': links_all, 'DownloadLink': dlinks_all, 'Name': dlinks_all_name}
template_list_df = pd.DataFrame(template_list)
print(template_list_df)

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "webscraping\presentationgo.csv"
template_list_df.to_csv(filename, encoding="cp1254", errors="ignore")

end_time = time.ctime()
print(f"End: {end_time}")
