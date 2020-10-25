"""
import time
def anafonksiyon(a,b):
    start1 = time.time()
    time.sleep(1)
    c = a + b
    finish1 = time.time()
    time1 = ("Fonksiyon süresi = " + str(finish1-start1))
    def fonk1(c):
        start2 = time.time()
        c = c**a
        time.sleep(1)
        finish2 = time.time()
        time2 = ("Fonksiyon süresi = " + str(finish2-start2))
        return c,time2
    def fonk2(c):
        start3 = time.time()
        time.sleep(1)
        c = c**b
        finish3 = time.time()
        time3 = ("Fonksiyon süresi = " + str(finish3-start3))
        return c,time3
    return c,time1,fonk1(c),fonk2(c)
print(anafonksiyon(2,154))
"""
"""
# Birden yüze kadar sayıların karelerinin toplamı ile toplamlarının karelerinin farkı
toplamkare = 0
toplamsayi = 0
for i in range(1,101):
    toplamsayi += i
    i +=1
for i in range(1,101):
    toplamkare = toplamkare + (i**2)
    i+=1
sonuc = (toplamsayi**2) - toplamkare
print(toplamsayi**2)
print(toplamkare)
print(sonuc)
"""
"""
bilgi = 
Pisagor Üçlüsü a<b<c ve a^2 + b^2 = c^2 olarak tanımlanabilir.
Örneğin ==> 3^2 + 4^2 = 9+16 = 5^2 = 25
a + b + c = 1000 sonucunu veren yukarıdaki kurala uyan yalnızca bir adet pisagor üçlüsü vardır.
Bu üçlü için (a * b * c) kaçtır?
def pisagor():
    for a in range(1,1001):
        for b in range(1,1001):
            c = 1000-a-b

            if (a**2) + (b**2) == (c**2):
                print(f"bu üçlü = {a} , {b} ve {c} sayılarıdır.")
                return a*b*c

print(bilgi)
print("çarpımları ise =  "+str(pisagor())+" dir")
"""






