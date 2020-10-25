from random import randint
def carpim(a,b,c):
    if c != "-1":
        result = str(a*b)
        if result == r:
            print("Doğru")
        else:
            print(f"Yanlış! Doğru cevap {r}")
    else:
        secim()
def basla(rng1,rng2):
    if rng1 > 10:
        x = 10
    else:
        x = 5
    for a in range(0,x):
        for b in range(0,x):
            sayi1 = randint(rng1,rng2)
            sayi2 = randint(rng1,rng2)
            print(f"{sayi1} x {sayi2} = ")
            sonuc = input("Cevabınız = ")
            carpim = sayi1,sayi2,sonuc

            if a == 4 and b == 4:
                print("Bölüm bitti")
                secim()
def secim():
    print(" Hangi seviyeden başlamak istiyorsunuz (çıkış = -1) ?\n")
    print("  1 - Kolay ")
    print("  2 - Orta ")
    print("  3 - Zor")
    print("  4 - Çok zor\n")

    svy = input("Seçiminiz = ")

    if svy =="1":
        basla(1,6)
        
    elif svy == "2":
        basla(6,12)
    
    elif svy == "3":
        basla(12,25)
    
    elif svy == "4":
        basla(25,100)

    else:
        exit(0)
if __name__ == "__main__":
    secim() 
"""
"""
import math
a = int(input("Faktöriyelini almak istediğiniz sayı = "))
result = math.factorial(a)
print(result)