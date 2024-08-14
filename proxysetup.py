import requests

url="https://parhailikhai.com/"

response = requests.get(url)

html=response.text

def savehtmltofile(html,path):
    with open(path,'w') as f:
        f.write(html)


savehtmltofile(html,"P:\Working Directories\Web Scrapping\htmlfile.html")
        