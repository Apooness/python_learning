import time
import requests
from bs4 import BeautifulSoup
lim = int(input("Kaç diziye bakmak istiyorsunuz? = "))
url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
liste = soup.find("tbody",{"class":"lister-list"}).findAll("tr",limit = lim)
count = 1
for i in liste:
    title = i.find("td",{"class":"titleColumn"}).find("a").text
    rating = i.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    year = i.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    print(f"{count}- dizi adı: {title.ljust(50)} yıl: {year.ljust(10)} değerlendirme: {rating}")
    count+=1
time.sleep(5)