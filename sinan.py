import requests
from bs4 import BeautifulSoup
from urllib import request

url = "https://en.wikipedia.org/wiki/David_Beckham"
html = request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

def getpersoninfo():
     nameObj = soup.find('h1')
     name = nameObj.find('span').text
     imageObj = soup.find('meta',property="og:image")
     image = imageObj['content']
     return name,image
name,image = getpersoninfo()
print('Name:',name)
print('Image',image)

# def addition():
#     output=12+30
#     return output
# result = addition()
# print(result)