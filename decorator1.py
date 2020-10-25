"""
def fonkisyon(*args):
    def topla(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(topla(args))

fonkisyon(1,25,51)
"""
"""
liste = []
while True:
    sayi = input("Sayı Giriniz(Çıkış için ==q) = ")
    if sayi == "q":
        break
    sayi = int(sayi)
    liste.append(sayi)
def anafonksiyon(islem_adi):
    def toplama(liste):
        toplam = 0
        for i in liste:
            toplam += i
        print(toplam)
    def carpma(liste):
        carpim = 1
        for i in liste:
            carpim *= i
        print(carpim)

    if islem_adi == "toplama":
        return toplama
    else:
        return carpma

secim = input("Yapmak istediğiniz işlem = ")
fonksiyon = anafonksiyon(secim)
fonksiyon(liste)
"""
"""
def toplama(a,b):
    return (a+b)
def cikarma(a,b):
    return(a-b)
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anafonksiyon(f1,f2,f3,f4,islem):
    if islem == "toplama":
        a = int(input("1. Sayı = "))
        b = int(input("2. Sayı = "))
        print(f1(a,b))

    elif islem == "cikarma":
        a = int(input("1. Sayı = "))
        b = int(input("2. Sayı = "))
        print(f2(a,b))
    
    elif islem == "carpma":
        a = int(input("1. Sayı = "))
        b = int(input("2. Sayı = "))
        print(f3(a,b))
    elif islem == "bolme":
        a = int(input("1. Sayı = "))
        b = int(input("2. Sayı = "))
        print(f4(a,b))
    else:
        print("Yanlış seçim!!!")

islem = input("Yapmak istediğiniz işlem")
anafonksiyon(toplama,cikarma,carpma,bolme,islem)
"""



