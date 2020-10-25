import requests
from bs4 import BeautifulSoup
lim = int(input("Kaç Diziye Bakmak istiyorsunuz(limit = 50) = "))
url = "https://dizilla.com/trend/"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
liste = soup.find("tbody").findAll("tr",limit = lim)
for i in liste:
    title = i.find("td",{"class":""}).find("span").text.strip()
    category = i.find("td",{"class":"text-white text-xxsmall"}).text.strip()
    rating = i.find("td",{"class":"text-center"}).text.strip()
    print(f"Dizi Adı: {title.ljust(25)} Kategori: {category.ljust(40)} imdb puanı: {rating.ljust(25)}")

    