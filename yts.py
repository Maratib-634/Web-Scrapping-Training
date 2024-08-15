import requests
from bs4 import BeautifulSoup
''''
#checking status of website
r=requests.get("https://yts.mx/")
print("Reponse",r)


#saving html of yts page into a file

html=r.text
path=r'P:\Working Directories\Web Scrapping\Web Scrapping Training\yts.html'
with open(path,'w',encoding='utf-8') as f:
    f.write(str(html))

'''

#lets create a soup of given html
path=r"P:\Working Directories\Web Scrapping\Web Scrapping Training\yts.html"

with open(path,'r',encoding='utf-8') as f:
    doc=f.read()
soup=BeautifulSoup(doc,'html.parser')
#print(soup.prettify())

#lets print the title of page
#print(soup.title.string)

""""
#finding all div tag
div_tag=soup.find_all("div")

#saving all the div tag into a text file
with open("P:\Working Directories\Web Scrapping\Web Scrapping Training\div_tag.txt",'w',encoding='utf-8') as file:
    file.write(str(div_tag))
"""



names=soup.find_all('a',class_="browse-movie-title")
#print(str(names))

for n in names:
    print(n.text)