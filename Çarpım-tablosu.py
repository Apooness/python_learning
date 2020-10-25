import time
def islem(sayi = 0):
    start = time.time()
    for i in range(0,21):
        print(f"{sayi} * {i} = {sayi*i}")
    print("Tablo bitti")
    finish = time.time()
    print("Fonksiyon " + str(finish-start)+" saniye sürdü")

while True:
    sayi = input("Hangi sayının çarpım tablosuna bakmak istiyorsunuz? (çıkış = h) = ")
    if sayi == "h":
        print("Çıkış yapıldı")
        break
    else:
        islem(int(sayi))
