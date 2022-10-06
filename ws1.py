import requests
from bs4 import BeautifulSoup
r=requests.get("https://en.wikipedia.org/wiki/Python")
a=BeautifulSoup(r.content, 'html.parser')
#print(a.title)
#print(a.title.name)
lines=a.find_all('h1')
for line in lines:
    print(line.text)
    lines=a.find_all('h2')
for line in lines:
    print(line.text)
    lines=a.find_all('h3')
for line in lines:
    print(line.text)
    lines=a.find_all('h4')
for line in lines:
    print(line.text)
    lines=a.find_all('h5')
for line in lines:
    print(line.text)
    lines=a.find_all('h6')
for line in lines:
    print(line.text)
    


