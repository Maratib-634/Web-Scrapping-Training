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

'''
# Find all movie sections
movie_sections = soup.find_all('div', class_='browse-movie-wrap')

# Extract details for each movie
movies = []

for movie in movie_sections:
    # Extract movie name
    movie_name_tag = movie.find('a', class_='browse-movie-title')
    movie_name = movie_name_tag.get_text(strip=True).replace('[GL]', '').replace('[EN]', '').strip() if movie_name_tag else 'none'

    # Extract year
    movie_year_tag = movie.find('div', class_='browse-movie-year')
    movie_year = movie_year_tag.get_text(strip=True) if movie_year_tag else 'none'

    # Extract rating
    rating_tag = movie.find('h4', class_='rating')
    rating = rating_tag.get_text(strip=True) if rating_tag else 'none'

    # Extract genre
    genre_tag = movie.find('figcaption').find('h4') if movie.find('figcaption') else None
    genre = genre_tag.get_text(strip=True) if genre_tag and genre_tag.text != 'Rating' else 'none'

    # Append extracted movie details to the list
    movies.append({
        'Name': movie_name,
        'Year': movie_year,
        'Rating': rating,
        'Genre': genre
    })

# Print results for all movies
for movie in movies:
    print(f"Movie Name: {movie['Name']}")
    print(f"Year: {movie['Year']}")
    print(f"Rating: {movie['Rating']}")
    print(f"Genre: {movie['Genre']}")
    print()

'''



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
    


""" #Lets create a dataframe to save this data
import pandas as pd
dct={"Titles":titles,"Years":year,"Rattings":rattings}
df=pd.DataFrame(dct)
#df=pd.DataFrame(list(zip(titles,year)),columns=['Titles','Year'])
print(df) """

