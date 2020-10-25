import math
import time

def zaman(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(0)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__ + " "+ str(finish-start) + " saniye sürdü")
    return inner
@zaman
def usalma(a,b):
    sonuc1 = math.pow(a,b)
    print(sonuc1)
@zaman
def faktoriyel(a):
    sonuc2 = math.factorial(a)
    print(sonuc2)

@zaman
def toplam(a,b):
    print(a+b)

toplam(10,20)
usalma(2,143)
faktoriyel(16)