"""
def total(num1,num2):
    return num1+num2

result = total(int(input("1. Sayı = ")),int(input("2. Sayı = ")))
print(result)
"""
"""
def toplam(num1,num2):
    print(num1+num2)

toplam(int(input("1. Sayı = ")),int(input("2. Sayı = ")))
toplam(int(input("1. Sayı = ")),int(input("2. Sayı = ")))
toplam(int(input("1. Sayı = ")),int(input("2. Sayı = ")))
toplam(int(input("1. Sayı = ")),int(input("2. Sayı = ")))
"""
"""
def hesap(r):
    pi = 3.14
    alan = (pi * (r**2))
    print("ALANI=",alan)

yaricap = int(input("Dairenin yarıçapı:"))

hesap(yaricap)
"""
"""
def asalmi(x):
    i = 2
    while i*i <=x:
        if x%i == 0:
            return False
        i +=1
    else:
        return True
sayi = int(input("Sayı Giriniz = "))
asalmi(sayi)
if asalmi == True:
    print("Sayı asal")
else:
    print("Sayı asal değil")
"""
"""
def carpanlar(a):
    x = 2
    while a>1:
        asal = True
        i = 2
        while i*i<=x:
            if x%i == 0:
                asal = False
                break
            i += 1

        if asal and a %x == 0:
            print(x)
            while a %x==0:
                a = a / x
        x +=1
N = int(input("Sayı giriniz = "))
carpanlar(N)
"""
"""
def liste(baslangıc):
    while baslangıc > 1:
        if baslangıc % 2 == 0:
            baslangıc = baslangıc / 2
        else:
            baslangıc = (3*baslangıc) + 1 
        print(int(baslangıc))
baslangıc = int(input("Başlangıç Değeri = "))
liste(baslangıc)
"""