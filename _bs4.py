from bs4 import BeautifulSoup
import requests

url = "https://www.webtekno.com"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
titleList = []
writerList = []
liste = soup.find("div",{"class":"content-timeline__list"}).findAll("div",{"class":"content-timeline__item"})
for i in liste:
    title = i.find("h3").text
    writer = i.find("a",{"class":"content-timeline__detail__author hide-phone"}).text
    titleList.append(title)
    writerList.append(writer)

i = 0
with open("webtekno.txt","w",encoding="UTF-8") as f:
    for t in titleList:
        msg = f"{t}\n"
        f.write(msg)
        i +=1