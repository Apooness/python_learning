"""
import time
start = time.time()
def cube():
    sonuc = []

    for i in range(5000):
        sonuc.append(i**3)
    return sonuc

print(cube())
stop = time.time()
print("Fonksiyon " + str(stop-start)+" saniye sürdü")
"""
"""
import time
start = time.time()
def cube():
    for i in range(5000):
        yield i**3

for i in cube():
    print(i)

stop = time.time()
print("Fonksiyon "+str(stop-start)+" saniye sürdü")
"""
"""
def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        a , b = b, a+b
        yield b
for sayi in fibonacci():
    if sayi > 1000000:
        break
    print(sayi)
"""
"""
class Karesi():
    def __init__(self, taban = 1 ,max = 0):
        self.max = max
        self.taban = taban
    def __iter__(self):
        return self
    def __next__(self):
        if self.taban<=self.max:
            sonuc = self.taban**2
            self.taban +=1
            return sonuc
        else:
            self.taban = 1
            raise StopIteration

baslangic = int(input("Hangi sayıdan başlansın kare alınmaya? = "))
bitis = int(input("Hangi sayıya kadar karesini almak istiyorsunuz? = "))
karesi = Karesi(baslangic,bitis)
for i in karesi:
    print(i)
"""
"""
def asalsayi(x):
    for i in range(2,x+1):
        sayac = 0
        for j in range(2,i):
            if i % j == 0:
                sayac +=1
        if sayac == 0:
            yield i

sayi = int(input("Hangi sayıya kadar olan asal sayılar bulunsun? = "))
for i in asalsayi(sayi):
    print(i)
"""






