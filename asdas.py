# def yazdir():
#     print("merhaba")
#     return "çalıştı"

# cevap = yazdir()
# print("Fonksiyon",cevap)

# def daire(r,pi = 3.14):
#     alan = pi*(r**2)
#     return (alan)
# # daire(15)
# cevap = daire(15)
# print(cevap)
"""
a = ['Mary', 'had', 'a', 'little', 'lamb']
b = range(len(a))
print(b)
"""
# print(sum(list(range(5))))
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            continue
    else:
        print(n, 'is a prime number')
print()
print()
"""
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
"""
"""
def fib(n):
    a,b = 1,1
    while a < n:
        print(a)
        a , b = b , a+b
fib(15)
"""
"""
sayi = 23
tahmin = int(input("Tahmin: "))
if tahmin == sayi:
    print("Doğru!!!")
else:
    print("yanlış!!!")
"""
"""
while True:
    a = input("Şifre: ")
    if len(a)<3 or len(a)>8:
        print("Parola 3-8 uzunluğunda olmalı!!!")
    elif a == "":
        print("Parola kısmı Boş olamaz!!!")
    else:
        print("Başarılı bir şekilde parola oluşturuldu...")
        break
"""
# print(*range(10),sep = "\n")
# for i in range(10):
#     print(i)
# for i in range(5):
#         print(i)
#         if i == 4:
#             break
# else:
#         print("else çalıştı.")
# karater_dizisi = "Bu yAzıdA küçük A yok."
# for harf in karater_dizisi:
#     if harf == 'a':
#         print("a harfi bulundu.")
#         break
#     else:
#         print("a harfi bulunmadı.")
#         break
# for i in dir(str):
#     print("%s" %i)
# print(complex(4))
# sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
# print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
# for i in range(17):
#     print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
# print(type(dict))
# dirs = dir(dict)
# for d in dirs:
#     if not d.startswith("_"):
#         print(d)
"""
from math import pi
class Shape(object):
    def __init__(self):
        self.area = 0.0
        self.perimeter = 0.0
    def calc_area(self):
        pass
    def calc_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, l):
        super(Rectangle, self).__init__()
        self.w = w
        self.l = l

    def calc_area(self):
        self.area = self.w * self.l
        return self.area
    
    def calc_perimeter(self):
        self.perimeter = 2*(self.w + self.l)
        return self.perimeter

class Circle(Shape):
    def __init__(self, r):
        super(Circle, self).__init__()
        self.r = r

    def calc_area(self):
        self.area = pi * (self.r ** 2)
        return self.area

    def calc_perimeter(self):
        self.perimeter = 2 * pi * self.r
        return self.perimeter

class Triangle(Shape):
    def __init__(self, b, s2, s3, h):
        self.b = b
        self.s2 = s2
        self.s3 = s3
        self.h = h

    def calc_area(self):
        self.area = 0.5 * self.b * self.h
        return self.area

    def calc_perimeter(self):
        self.perimeter = self.b + self.s2 + self.s3
        return self.perimeter

s = Rectangle(10, 20)
print ("Rectangle - area: %.2f\tperimeter: %.2f" % (s.calc_area(), s.calc_perimeter()))
c = Circle(2)
print ("Circle - area: %.2f\tperimeter: %.2f" % (c.calc_area(), c.calc_perimeter()))
t = Triangle(3, 2, 2, 2.5)
print ("Triangle - area: %.2f\tperimeter: %.2f" % (t.calc_area(), t.calc_perimeter()))
"""
# def collatz(number):
#     step = 0
#     while number != 1:
#         if number%2 == 0:
#             print(int(number/2))
#             number = number/2
#             step += 1
#         else:
#             print(int((number*3)+1))
#             number = (number*3)+1
#             step += 1
#     print("Adım Sayısı: "+str(step))

# number = int(input("Bir Sayı Giriniz: "))
# collatz(number)

