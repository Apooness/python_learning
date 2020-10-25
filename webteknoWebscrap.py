from bs4 import BeautifulSoup
import requests


# def webscrap(url):
#     html = requests.get(url).content
#     soup = BeautifulSoup(html,"html.parser")
#     titleList = []
#     writerList = []
#     liste = soup.find("div",{"class":"content-timeline__list"}).findAll("div",{"class":"content-timeline__item"})

#     for i in liste:
#         title = i.find("h3").text
#         titleList.append(title)
#         writer = i.find("a",{"class":"content-timeline__detail__author hide-phone"}).text
#         writerList.append(writer)
#     for news in zip(titleList,writerList):
#         print(news)
#         print()

  
# webscrap("https://www.webtekno.com")
