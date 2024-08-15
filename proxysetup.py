import requests
from bs4 import BeautifulSoup


"""""
url="https://webscraper.io/test-sites"
response =requests.get(url)



#response of website
response = requests.get(url)

#download html of website
html=response.text


#function to save html in file
def savehtmltofile(html,path):
    with open(path,'w') as f:
        f.write(html)


savehtmltofile(html,"P:\Working Directories\Web Scrapping\htmlfile.html")


 """

#lets save the html using beautiful soup or lets create a soup of website
'''
soup=BeautifulSoup(response.text,'html.parser')
path=r"P:\Working Directories\Web Scrapping\Web Scrapping Training\file.html"
with open(path,'w') as file:
    file.write(str(soup))

'''
path=r'P:\Working Directories\Web Scrapping\Web Scrapping Training\file.html'
with open(path,'r') as file:
    doc=file.read()
soup=BeautifulSoup(doc,'html.parser')


print(soup.title.string)
