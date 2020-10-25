"""
print("Press 1 for Kelvin to Celcius")
print("Press 2 for Celcius to Kelvin")

choice = int(input("Your choice(1-2) = "))

if choice == 1:
    kelvin1 = int(input("Degree for convert = "))
    celcius1 = kelvin1 - 273
    print(f"Converted degree = {celcius1}")

elif choice == 2:
    celcius2 = int(input("Degree for convert = "))
    kelvin2 = celcius2 + 273
    print(f"Converted degree = {kelvin2}")

else:
    print("Wrong Choice")
"""
"""
def fizzbuzz(n):
    if n %3 == 0 and n %5 == 0:
        print("FizzBuzz")
    elif n %5 == 0:
        print("Buzz")
    elif n %3 == 0:
        print("Fizz")
    else:
        print(str(n))

fizzbuzz(len(input("Your Entry = ")))
"""
"""
last = int(input("Son sayı = "))
for i in range(1,last+1):
    print(i)
"""
"""
kısak = int(input("Kısa Kenar = "))
uzunk = int(input("Uzun Kenar = "))
secim = int(input("Alan = 1\nÇevre = 2\nSeçiminiz(1-2) = "))

if secim == 1:
    print(kısak*uzunk)
else:
    print(2*(kısak+uzunk)) 
"""
"""
kelime = input("Kelimeniz = ")
sayac = 0
while sayac<len(kelime):
    print(kelime[sayac])
    sayac +=1
print("Kelimenizi listeledim")
"""
"""
sayi1 = int(input("Küçük sayı = "))
sayi2 = int(input("Büyük sayı = "))
toplamcift = 0
toplamtek = 0
for i in range(sayi1,sayi2+1):
    if i % 2 == 0:
        toplamcift += i
    else:
        toplamtek += i
    
print(f"2 sayı arasındaki tek sayıların toplamı = {toplamtek}")
print(f"2 sayı arasındaki çift sayıların toplamı = {toplamcift}")
"""
"""
maas = int(input("Maaşınız = "))
zam = int(input("Zam Oranı = "))
yenimaas = maas + ((maas *zam)/100)
print(f"Yeni maaşınız = {yenimaas}")
"""
"""
def daire(yaricap):
    secim = int(input("Alan için 1\nÇevre için 2\nSeçiminiz = "))
    pi = 3.14
    if secim == 1:
        alan = pi*(yaricap**2)
        print(alan)
    else:
        cevre = 2*pi*yaricap
        print(cevre)

daire(int(input("Dairenin Yarıçapı = ")))
"""
"""
from random import randint
rand = randint(1,10)
sayac = 0

while True:
    sayac +=1
    sayi = int(input("Tahmininiz = "))
    if sayi == 0:
        print("Oyundan çıkılıyor")
        break
    elif sayi < rand:
        print("Yukarı")
        continue
    elif sayi > rand:
        print("Aşağı")
        continue
    else:
        print("Doğru Bildiniz")
        print(f"{sayac}. hakkınızda bildiniz") 
        break
"""
"""
sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
sayac = 0
for i in sayilar:
    if i % 5 == 0:
        print(str(i)+" 5'in katıdır.")
        sayac += 1
else:
    print("Döngü Bitti")
    print(f"Toplam {sayac} tane 5'in katı sayı var")
"""
"""
def ciftmi(x):
    x % 2 == 0
toplam = 0
sayac = 0
baslangic =int(input("Başlangıç Değeri = ")) 
bitis =int(input("Bitiş Değeri = "))
for sayi in range(baslangic,bitis+1):
    if ciftmi(sayi):
        toplam =toplam + sayi
        sayac +=1
print("Ortalama = ",(toplam/sayac))
"""
"""
class Sınıf:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
    no = "unknown"


o1 = Sınıf("Mustafa","Akil")
o2 = Sınıf("Berna","Dost")
print(o1.ad + ' ' + o1.soyad)
print(o2.ad+ ' '+o2.soyad)
o2.no = "221"
print(o2.no)
"""  
"""
class Person:
    def __init__(self,name,surname,year):
        self.name = name
        self.surname = surname
        self.year = year
        
    def age(self):
        return 2020 - self.year
        
    def selam(self):
        print(f"Merhaba Benim adım {self.name} soyadım {self.surname}")

p1 = Person("Mustafa","Akil",2001)
print(f"Adım {p1.name} soyadım {p1.surname} yaşım {p1.age()}")
# print(p1.name+" "+p1.surname+" "+str(p1.age()))
"""
"""
class Circle:
    pi = 3.14
    def __init__(self,yaricap = 1):
        self.yaricap = yaricap
    def cevre(self):
        return 2 * self.pi * self.yaricap

    def alan(self):
        return self.pi * (self.yaricap**2)

r1 = int(input("Yarıçap = "))
c1 = Circle(r1)
print(f"{r1} yarıçaplı çemberin çevresi {c1.cevre()} Alanı {c1.alan()}")
"""
"""
class Person:
    def __init__(self,name,surname,year):
        self.name = name
        self.surname = surname
        self.year = year

    def age(self):
        return 2020 - self.year
    def eat(self):
        print("I am eating")
    def run(self):
        print("I am running")

class Student(Person):
    def __init__(self, name, surname, year, number):
        Person.__init__(self, name, surname, year)
        self.number = number

class Teacher(Person):
    def __init__(self, name, surname, year, branch):
        super().__init__(name, surname, year)
        self.branch = branch

p1 = Person("Mustafa","Akil",2001)
s1 = Student("Berna","Dost",2002,"221")
t1 = Teacher("Sema","Koncalı",2002,"Music")

print(f"My Name is {p1.name} surname is {p1.surname} and i am {p1.age()} ")
print(f"My Name is {s1.name} surname is {s1.surname} i am {s1.age()} and my number is {s1.number} ")
print(f"My Name is {t1.name} surname is {t1.surname} i am {t1.age()} an my branch is {t1.branch} ")
"""
"""
liste = [(3, 4), (10, 3), (5, 6), (1, 9)]
def alan_hesapla(x):
    return x[0] * x[1]
print(list(map(alan_hesapla,liste)))
"""
"""
# Python "da dosyaya yazma ve dosyadan okuma programı
def Listeleme(dosyaAdi):
# Parametre olarak gelen dosyada bulunan kayıtları listeleme.
# Okumak için dosyanın açılması
    with open(dosyaAdi) as f: # f adında bir dosya nesnesi oluşturuldu
        print(f._CHUNK_SIZE)
        for satir in f: # Satır satır okuma işlemi için döngü kuruldu
            print(int(satir)) # int veri türüne dönüştürme ve ekrana yazdırma
def Kaydet(dosyaAdi):
    # Parametre olarak gelen dosyada bulunan kayıtları kaydetme.
    with open(dosyaAdi, "w") as f:  # f adında yazma modunda bir dosya nesnesi oluşturuldu
        sayi = 0
        while sayi != 999:  # Kullanici 999 giresiye kadar dönen döngü kuruluyor
            sayi = int(input("Lütfen sayi giriniz..(Çıkış için 999):"))
            if sayi != 999:
                f.write(str(sayi) + "\n")  # String veri türüne dönüşüm ve dosyaya kayıt
            else:
                break  # Döngüden çıkış
def main():
    # Ana Program başlangıcı. Menülü seçim işlemleri ve çıkış.
    while True:
        secim = input("(K)aydet (L)isteleme (S)onlandır: ")
        if secim == "K" or secim == "k":
            DosyaAdi =input("Kayıt Edilecek Dosya Adı Girin:")
            dosyaAdi = DosyaAdi+".txt"
            Kaydet(dosyaAdi)
        elif secim == "L" or secim == "l":
            DosyaAdi = input("Kayıtların Okunacağı Dosya Adını Girin: ")
            dosyaAdi = DosyaAdi+".txt"
            Listeleme(dosyaAdi)
        elif secim == "S" or secim == "s":
            break
main()
"""





