import random
ustsinir = int(input("Sayı tahmin oyunu en fazla kaç olsun = "))
sayi = random.randint(0,ustsinir+1)
hak = int(input("Kaç hakkınız olsun = "))
sayac = 0
while True:
    tahmin = int(input("Tahmininiz = "))
    if hak == sayac:
        break
    else:
        sayac+=1
        if tahmin == sayi:
            print("Doğru tahmin!!!")
            print(str(sayac)+". hakkınızda buldunuz")
            break

        elif tahmin < sayi:
            print("Yukarı")
            
        elif tahmin > sayi:
            print("Aşağı")
            
