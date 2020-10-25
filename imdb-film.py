import requests
from bs4 import BeautifulSoup
lim = int(input("İlk kaç filmi görmek istiyorsunuz?(sınır 250'dir) = "))
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
liste = soup.find("tbody",{"class":"lister-list"}).findAll("tr",limit = lim)
count = 1
for i in liste:
    title = i.find("td",{"class":"titleColumn"}).find("a").text
    year = i.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rate = i.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}- film adı: {title.ljust(50)} çıkış yılı: {year.ljust(20)} değerlendirme: {rate}")
    count += 1
