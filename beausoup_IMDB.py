
#IMDB TOP 250

import requests
URL = "https://www.imdb.com/chart/top/"
response = requests.get(URL)
#print(response.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

#<td class="titleColumn">

movies = soup.find_all('td',{'class':'titleColumn'})

#list comprehension
#bs4

movies_list = [movie.get_text().split('\n') for movie in movies]

isim =[]
yil =[

]
for movie in movies_list:
    isim.append(movie[2].strip())
    yil.append(movie[3])

rating = soup.find_all('td',{'class':'ratingColumn imdbRating'})
puan = [x.get_text().strip() for x in rating]

#print(puan)

import pandas as pd
imdb_dict = {'Name':isim, 'Year':yil, 'Rating':puan}
imdb_df = pd.DataFrame(imdb_dict)
print(imdb_df)