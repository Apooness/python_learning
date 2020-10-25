# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 
"""
def yazdir(kelime,adet):
    print(kelime*adet)

kelime = input("Yazdırmak istediğin kelime = ")
adet = int(input("Kaç defa = "))
yazdir(kelime,adet)
"""


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
"""
def listeyecevir(*params):
    liste = []
    for param in params:
        liste.append(param)

    return liste

result = listeyecevir(10,503,445,"ali","veli")
print(result)
"""


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
"""
def asalmi(a,b):
    for sayi in range(a,b+1):
        if sayi > 1:
            for i in range(2,sayi):
                    if sayi%i == 0:
                        break
            else:
                print(sayi)

baslangic = int(input("Sayı Giriniz = "))
bitis = int(input("Sayı Giriniz = "))
asalmi(baslangic,bitis)
"""

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
def bolenler(a):
    bolenler =[]

    for i in range(2,a):
        if sayi % i == 0:
            bolenler.append(i)
    print(bolenler)

sayi = int(input("Sayı Giriniz = "))
bolenler(sayi)



