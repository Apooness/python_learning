"""
import random
tutulan = random.randint(1,10)
sayac = 0
while True:
    sayac +=1
    tahmin = int(input("Tahmininiz = "))
    if tahmin == tutulan:
        print(f"Tebrikler! {sayac}. denemede bildiniz.")
        break
    elif tahmin < tutulan:
        print("Yukarı")
        continue
    else:
        print("Aşağı")
        continue
"""
"""
import math

a = int(input("Kökünü almak istediğiniz Sayı = "))
b = int(input("Faktöriyelini almak istediğiniz Sayı = "))

kok = math.sqrt(a)
kare = math.factorial(b)

print(kok,kare)
"""
"""
import math
secim = int(input("Seçiminiz(1-Kök Alma / 2-Faktöriyel Alma) = "))
if secim == 1:
    kok = math.sqrt(int(input("Kökünü Almak istediğiniz sayı = ")))
    print(kok)
    # kok = sayı ** 1/2
elif secim == 2:
    fact = math.factorial(int(input("Faktöriyelini almak istediğiniz Sayı = ")))
    print(fact)
else:
    print("Hatalı Seçim")
"""
"""
import os
import datetime
tarih = str(datetime.date.today()).replace("-",".")
print(tarih)
"""
"""
import math
sayi = float(input("Hangi sayının Karekökü alınsın? = "))
islem = math.sqrt(sayi)
print(islem)
"""
"""
def yardim():
    print("Topla : 2 sayıyı Toplar.")
    print("Fark Alma : 2 sayıyı birbirinden çıkarır.")
    print("Bölme : 2 sayıyı birbirine böler.")
    print("Yazdır : En Son işlemin sonucunu yazdırır.")
def menu():
    return input("Seçiminiz = (T)opla - (F)ark Alma - (B)ölme - (Y)azdır - Y(a)rdım -  (Ç)ıkış = ")
def islem():
    sonuc = 0.0
    done = False
    while not done:
        secim = menu()
        if secim == "Ç" or secim == "ç":
            print("Çıkılıyor")
            done = True
        elif secim == "T" or secim == "t":
            s1 = float(input("1. Sayı = "))
            s2 = float(input("2. Sayı = "))
            sonuc = s1+s2
            print(sonuc)
        elif secim == "F" or secim == "f":
            s1 = float(input("Büyük sayı = "))
            s2 = float(input("Küçük sayı = "))
            sonuc = s1-s2
            print(sonuc)
        elif secim == "B" or secim == "b":
            s1 = float(input("Bölünen sayı = "))
            s2 = float(input("Bölen sayı = "))
            sonuc = s1/s2
            print(sonuc)
"""

        elif secim == "A" or secim == "a":
            yardim()
        
        else:
            print(sonuc)
            
islem()


