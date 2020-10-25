import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu-aksesuarlari/cep-telefonu-kulaklik?btt=Kablolu"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
liste = soup.findAll("li",{"class":"column"})
for i in liste:
    title = i.div.a.h3.text.strip()
    oldprice = i.find("div",{"class":"proDetail"}).findAll("a")[0].text.strip().strip("TL")
    newprice = i.find("div",{"class":"proDetail"}).findAll("a")[1].text.strip().strip("TL")
    SallerName = i.find("a",{"class":"sallerInfo"}).find("span",{"class":"sallerName"}).text.strip()
    rating = i.find("a",{"class":"sallerInfo"}).find("div",{"class":"shopPoint"}).text.strip()
    print(f"ürün adı: {title} eski fiyatı: {oldprice} yeni fiyatı: {newprice} Satıcı: {SallerName} Puanı: {rating}")