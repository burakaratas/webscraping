
#Piyasa Değerine Göre Bankalar

import requests
from bs4 import BeautifulSoup

URL = "https://companiesmarketcap.com/banks/largest-banks-by-market-cap/?page="
nr_pages = 5


bank_list_all = []
bank_code_list_all = []
bank_country_list_all = []
mcap_price_list_all = []
order_list_all = []
mcap_list_all = []
price_list_all = []

for i in range(nr_pages):
    URLtogo = URL+str(i+1)
    response = requests.get(URLtogo)
    soup = BeautifulSoup(response.content, 'html.parser')

    banks = soup.find_all('div',{'class':'company-name'})
    bank_list = [bank.get_text().strip() for bank in banks]

    bank_codes = soup.find_all('div',{'class':'company-code'})
    bank_code_list = [bank_code.get_text() for bank_code in bank_codes]

    bank_country = soup.find_all('span',{'class':'responsive-hidden'})
    bank_country_list = [country.get_text() for country in bank_country]
    bank_country_list.pop(0)

    mcap_prices = soup.find_all('td',{'class':'td-right'})
    mcap_price_list = [mcap_price.get_text() for mcap_price in mcap_prices]

    order_list = []
    mcap_list = []
    price_list = []

    for x in range(len(mcap_price_list)):
        if x % 3 == 0:
            order_list.append(mcap_price_list[x])
        if x % 3 == 1:
            mcap_list.append(mcap_price_list[x])
        if x % 3 == 2:
            price_list.append(mcap_price_list[x])

    bank_list_all.extend(bank_list)
    bank_code_list_all.extend(bank_code_list)
    bank_country_list_all.extend(bank_country_list)
#   order_list_all.extend(order_list)
    mcap_list_all.extend(mcap_list)
#   price_list_all.extend(price_list)

import pandas as pd
bank_dict = {'Name':bank_list_all, 'Country': bank_country_list_all, 'Mcap':mcap_list_all, 'Code':bank_code_list_all}
bank_dict_df = pd.DataFrame(bank_dict)
print(bank_dict_df)

filename = "webscraping\largestbanks.csv"
bank_dict_df.to_csv(filename, encoding="utf-8", errors="ignore")

filter_bank_dict = bank_dict_df.loc[bank_dict_df['Country'].str.contains("Turkey")]
print(filter_bank_dict)