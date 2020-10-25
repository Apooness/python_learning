"""
#Kullanıcıya dik üçgen, kare ve dikdörtgenden hangisi ile işlem yapmak istediğini sorarak aldığı cevaba göre bu şekillerin alan ve çevresini hesaplayıp yazdıran programı yazınız.
def dik_ucgen():
    k1 = int(input("Üçgenin 1. Dik kenarı = "))
    k2 = int(input("Üçgenin 2. Dik kenarı = "))
    k3 = (k1**2 + k2**2) ** 0.5
    print("üçgenin alanı = ",(k1*k2)/2)
    print("Üçgenin Çevresi = ",k1+k2+k3)
def kare():
    k = int(input("Karenin kenarı = "))
    print("Karenin alanı = ",k*k)
    print("Karenin çevresi = ",k*4)
def dikdortgen():
    k1 = int(input("Dikdörtgenin uzun kenarı = "))
    k2 = int(input("Dikdörtgenin kısa kenarı = "))
    print("Dikdörtgenin alanı = ",k1*k2)
    print("Dikdörtgenin Çevresi = ",(k1+k2)*2)

def Secim():
    secim = input("1- Dik Üçgen\n2- Kare\n3- Dikdörtgen\nSeçiminiz = ")
    if secim == "1":
        dik_ucgen()
    elif secim == "2":
        kare()
    else:
        dikdortgen()
Secim()
"""
"""
#Kullanıcın adını ve soyadını isteyerek bir tam ad fonksiyonu ile değer dönderen bir fonksiyon tanımlayınız.
def tamad():
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    return ad+" "+soyad
print(tamad())
"""
"""
#Kullanıcıdan 0-100 aralığında sayılar isteyerek 50 büyük girdiği sayıların toplamını, 50 küçük girdiği sayıların ise adetini yazdıran programı yazınız. 50 girildiğinde ise program sonuçları bildirecektir.
toplam = 0
adet = 0
while True:
    sayi = int(input("Sayı giriniz(Çıkmak için '50' basınız) = "))
    if sayi == 50:
        print("50den büyük sayıların toplamı = ",toplam)
        print("50den küçük sayıların adedi = ",adet)
        break
    else:
        if sayi >50:
            toplam = toplam + sayi
        else:
            adet +=1
"""
"""
#Girilen sayının faktöriyelini hesaplayan fonksiyonları yazınız.
from math import factorial 
def fak():
    while True:
        sayi = int(input("Faktöriyelini alam istediğiniz sayı(çıkış için 0) = "))
        if sayi == 0:
            print("Çıkılıyor")
            break
        else:
            print(factorial(sayi))
fak()
"""
#Kullanıcın tuttuğu sayıyı tahmin etmeye çalışan bir fonksiyon yazınız. 

