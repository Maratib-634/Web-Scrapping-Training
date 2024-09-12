'''
PROJECT REQUIREMENTS:
1. Movies, year, Rating, Genre
2. Save them in pandas
3. Do some analysis
4. Scrapping from multiple pages

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


#<<<<<<<<<<<<<<<Printing the information one by one from each movie>>>>>>>>>>>>>>>>>>>>

""" 
#Titles of all the movies on page
titles=[]
T=soup.find_all('a',class_="browse-movie-title")

i=0
for t in T:
    titles.append(t.text)
    i=i+1
    #print(i,":",t.text)

#lets save the year of release 
year=[]
Y=soup.find_all('div',class_="browse-movie-year")

for y in Y:
    year.append(y.text)
    #print(y.text)


#lets save the ratings of movies 

rattings=[]
R=soup.find_all('h4',class_="rating")

i=0
for r in R:
    rattings.append(r.text)
    i+=1
    #print(i,":",r.text)

rattings.insert(5,"5/10")
rattings.insert(9,"5.5/10")
rattings.insert(18,"4.5/10")


#lets scrap the genres of movies
Genre=[]
genre=soup.find_all('h4')

for g in genre:
    Genre.append(g.text)
    print(g.text)

 """


#CASE : some times of we have scrape data which are in realtionship like ratings have relation with movies 
# so in case if some movies does'nt have any rating how would we handle that......
# Below is the explaination of that

#first search for movie block print class not its tag
movies=soup.find_all(class_="browse-movie-wrap")

for movie in movies:
    title_tag=movie.find('a',class_='browse-movie-title')
    title=title_tag.text.strip() if title_tag else "No Title"
    print(title)

# Extract the rating
    rating_tag = movie.find('h4', class_='rating')
    rating = rating_tag.text.strip() if rating_tag else 'Rating not available'
    print(rating)
    


    #****..........continue with similar code...........*****


""" #Lets create a dataframe to save this data
import pandas as pd
dct={"Titles":titles,"Years":year,"Rattings":rattings}
df=pd.DataFrame(dct)
#df=pd.DataFrame(list(zip(titles,year)),columns=['Titles','Year'])
print(df) """



#*****Lets Scrape the data from Multiple pages Using beautiful_Soup******
#Search for NEXT tag(move towards next page) >> create its soup >> Create Loop >> Iterate to each page to extract data




""" #lets get url of each page
url="https://yts.mx/browse-movies"
response=requests.get(url)
html=response.text
soup=BeautifulSoup(html,"html.parser") """
#print(soup)
titles=[]
years=[]
rattings=[]
genres=[]


for i in range(1,10):
    url=url="https://yts.mx/browse-movies"+"?page="+str(i)
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html,"html.parser")


    
    block=soup.find_all('div',class_="browse-movie-wrap")
   

    for movie in block:
        title_tag=movie.find('a',class_='browse-movie-title')
        title=title_tag.text.strip() if title_tag else "No title"
        titles.append(title)


        year_tag=movie.find('div',class_='browse-movie-year')
        year=year_tag.text.strip() if year_tag else "No Year"
        years.append(year)

        ratting_tag=movie.find('h4',class_="rating")
        ratting=ratting_tag.text.strip() if ratting_tag else "No rattings"
        rattings.append(ratting)


        genre=[genre.text.strip() for genre in movie.find_all('h4') if genre.get('class') is None]
        if not genre:
            genre=["No genre"]
        genres.append(genre)


                
       
        """ print(f"Title: {title}")=-mnmgfe3
        print(f"Year: {year}")
        print(f"Rating: {ratting}")
        print(f"Genres: {', '.join(genre)}")
        print("-" * 40)   """

""" 
print(len(titles))
print(len(years))
print(len(rattings))
print(len(genres))
     """
    
       

import pandas as pd
dict={"Titles":titles,"Years":years,"Rattings":ratting,'Genre':genres}
df=pd.DataFrame(dict)
df.to_csv("YTS_movies.csv",index=False)
#print(df) 


