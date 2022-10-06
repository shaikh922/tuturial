'''
import requests
r=requests.get("https://www.w3schools.com/default.asp")
print(r.content)
print(r.url)
from bs4 import BeautifulSoup
#find all function in beautifulsoup is use to find tags in html output.
a=BeautifulSoup(r.content, 'html.parser')
b=a.find('div',class_='w3-main')
lines=a.find_all('p')
for line in lines:
    print(line.text)
'''

import requests
r=requests.get("https://en.wikipedia.org/robots.txt")
print(r.content)
'''from bs4 import BeautifulSoup
#find all function in beautifulsoup is use to find tags in html output.
a=BeautifulSoup(r.content, 'html.parser')
lines=a.find_all('p')
for line in lines:
    print(line.text)
    
for line in lines:
    if 'href' in line.attrs:
        print(line.attrs['href'])
        
'''
