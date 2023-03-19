
# DENENİYOR
# https://www.kap.org.tr/tr/api/disclosures?ts=638647299&fromDate=2023-02-23&toDate=2023-02-23&memberTypes=IGS-DDK
# https://www.kap.org.tr/tr/api/disclosures?fromDate=2023-02-23&toDate=2023-02-23&memberTypes=IGS-DDK

#Suprise motherfucker

import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import pandas as pd
import numpy as np
import time
import json

start_date = '2023-02-24'
end_date = '2023-02-24'

b = Browser()
b.set_handle_robots(False)
b.addheaders = [('Referer', 'https://www.kap.org.tr'), ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41')]

#Oid için adımlar
#https://www.kap.org.tr/tr/bist-sirketler
#https://www.kap.org.tr/tr/sirket-bilgileri/ozet/2413-akbank-t-a-s
#<a class="w-inline-block tab-subpage _01" href="/tr/sirket-finansal-bilgileri/4028e4a240e8d1830140e905edcd0006">
#https://www.kap.org.tr/tr/sirket-finansal-bilgileri/4028e4a240e8d1830140e905edcd0006


#https://www.kap.org.tr/tr/api/disclosures?ts=625616924&fromDate=2023-02-24&toDate=2023-02-24&memberTypes=IGS-DDK-YK&companyOid=4028e4a240e8d1830140e905edcd0006
URL = "https://www.kap.org.tr/tr/api/disclosures?fromDate=" + start_date + "&toDate=" + end_date + "&memberTypes=IGS-DDK"
URLtogo = URL
b.open(URLtogo)
soup = BeautifulSoup(b.response().read(), 'html.parser')

table = json.loads(str(soup))
table1 = [item.get('basic') for item in table]
table2 = [item.get('detail') for item in table]
table1 = pd.DataFrame(table1)
table2 = pd.DataFrame(table2)
#print(table)
print(table1)
print(table2)



timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "webscraping\KAP" + timestr + ".csv"
table1.to_csv(filename, encoding="cp1254", errors="ignore")
