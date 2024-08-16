'''
PROJECT REQUIREMENTS:
1. Movies, year, Rating, Genre
2. Save them in pandas
3. Do some analysis

'''


#importing libraries
import requests
from bs4 import BeautifulSoup

"""
#lets parse the html of yts browse page 
url="https://yts.mx/browse-movies"
response=requests.get(url,'html.parser')
html=response.text


#lets save the html in website in movies.html file
path=r"P:\Working Directories\Web Scrapping\Web Scrapping Training\movies.html"
with open(path,'w',encoding='utf-8')as f:
    f.write(html)
"""

#creating soup of html file
path=r"P:\Working Directories\Web Scrapping\Web Scrapping Training\movies.html"
with open(path,'r',encoding="utf-8") as f:
    s=f.read()

soup=BeautifulSoup(s,'html.parser')
#print(soup.prettify())



#Titles of all the movies on page
titles=[]
T=soup.find_all('a',class_="browse-movie-title")

for t in T:
    titles.append(t.text)
    #print(t.text)

#lets save the year of release 
year=[]
Y=soup.find_all('div',class_="browse-movie-year")

for y in Y:
    year.append(y.text)
    #print(y.text)

"""
#lets save the ratings of movies 
rattings=[]
R=soup.find_all('h4',class_="rating")

for r in R:
    rattings.append(r.text)
    print(r.text)

"""




#Lets create a dataframe to save this data
import pandas as pd
dct={"Titles":titles,"Years":year}
df=pd.DataFrame(dct)
#df=pd.DataFrame(list(zip(titles,year)),columns=['Titles','Year'])
print(df)

