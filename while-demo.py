sayilar = [1,3,5,7,9,12,19,21]
"""
# 1: sayilar listesini while ile ekrana yazdırın.
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1
"""
"""
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
ilk = int(input("Başlangıç değeri = "))
son = int(input("Bitiş değeri = "))
i = ilk
while i < son:
    i += 1
    if i % 2 == 1:
        print(i)
"""
"""
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
ilk = 100

while ilk > 0:
    print(ilk)
    ilk -=1
"""
"""
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []
i = 0
while i < 5:
    sayi = int(input("1. Sayı = "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
"""
"""
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input("Kaç Adet? = "))
i = 0
while i < adet:
    name = input("Ürün adı = ")
    price = input("Ürün Fiyatı = ")
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1

for urun in urunler:
    print(f"Ürün adı = {name}\nÜrün fiyatı = {price}")

"""