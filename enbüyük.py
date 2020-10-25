liste = []
while True:
    sayi = input("Sayı giriniz(çıkmak için == q) = ")
    if sayi == "q":
        print("Çıkış yapılıyor!!!")
        break
    sayi = int(sayi)
    liste.append(sayi)
liste.sort()
print(f"Listenin en küçük değeri = {liste[0]}")
print(f"Listenin en büyük değeri = {liste[-1]}")