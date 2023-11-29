# from urllib import request
# from bs4 import BeautifulSoup
# from urllib.request import Request
#
# url = "https://m.imdb.com/title/tt0111161/?ref_=chttp_i_1"
# url_request = Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
# html = request.urlopen(url_request).read()
# soup = BeautifulSoup(html,'html.parser')
#
# def movieInfo():
#     nameObj = soup.find('h1')
#     name = nameObj.find('span').text
#     directObj = soup.find('a',{'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}).text
#     yearObj = soup.find('div',{'class':'sc-9aa2061f-0 cyMUeu'})
#     year = yearObj.find('a',{'class':'ipc-link ipc-link--baseAlt ipc-link--inherit-color'}).text
#     genreObj = soup.find('div',{'class':'ipc-chip-list__scroller'})
#     genre = genreObj.find('span').text
#     imageObj = soup.find('meta',property="og:image")
#     image = imageObj['content']
#     rateObj = soup.find('div',{'class':'sc-bde20123-2 cdQqzc'})
#     rate = rateObj.find('span',{'class':'sc-bde20123-1 cMEQkK'}).text
#
#     return name,directObj,year,genre,image,rate
# name,director,year,genre,image,rate = movieInfo()
# print('Movie:',name)
# print('Director:',director)
# print('Year:',year)
# print('Genre:',genre)
# print('Poster:',image)
# print('Rating:',rate)




#import required libraries
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import Request
import requests
import json

url = "https://m.imdb.com/title/tt0108052/?ref_=chttp_t_6"
#new url is going to be url_request
url_request = Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
html = request.urlopen(url_request).read()
soup = BeautifulSoup(html,"html.parser")

def soupFunction(url):
    url_request = Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
    html = request.urlopen(url_request).read()
    soup = BeautifulSoup(html,"html.parser")
    return soup


#function to access all links
def allLinks():
    urls = set()
    soup = soupFunction("https://m.imdb.com/chart/top/")
    for i in soup.findAll("a"):
        link = i.get("href")
        if link and  link.startswith('/title/tt'):
            full_link = "https://m.imdb.com"+link.strip()
            urls.add(full_link)
    return list(urls)

def getMoviesinfo():
    dataList =[]
    myMovies  =allLinks()
    for i in myMovies[:50]:
        soup = soupFunction(i)

        nameObj = soup.find('h1')
        name = nameObj.find('span').text
        directObj = soup.find('a',{'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}).text
        yearObj = soup.find('div',{'class':'sc-9aa2061f-0 cyMUeu'})
        year = yearObj.find('a',{'class':'ipc-link ipc-link--baseAlt ipc-link--inherit-color'}).text
        genreObj = soup.find('div',{'class':'ipc-chip-list__scroller'})
        genre = genreObj.find('span').text
        rateObj = soup.find('div', {'class': 'sc-bde20123-2 cdQqzc'})
        rate = rateObj.find('span',{'class':'sc-bde20123-1 cMEQkK'}).text


        myData = {
            "Name":name,
            "Year":year,
            "Genre":genre,
            "Rating":rate
        }
        dataList.append(myData)

    jsonFile = open("myAllMovies.json","w")
    json.dump(dataList,jsonFile)


if __name__=="__main__":
    getMoviesinfo()
