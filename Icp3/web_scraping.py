import os
from bs4 import BeautifulSoup
import requests

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(html.text, "html.parser")
print(bsObj.title.string)
print(bsObj.findAll("a"))
for link in bsObj.findAll("a"):
    print(link.get('href'))
newobj=bsObj.findAll('div',{'id':"toc"})
print(newobj)
