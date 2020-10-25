
"""
# ilk 100 sayının toplamının karesinin ilk 100 sayının karesi toplamının farkı

toplam1 = 0
toplam2 = 0

for i in range(1,101):
    toplam1 = i + toplam1

for i in range(1,101):
    toplam2 = (i**2) + toplam2

sonuc = toplam2 - toplam1
print(sonuc)
"""
"""
# 2 uzeri 100 sayisinin basamak toplami
sayi = 2**100
sayi = str(sayi)
toplam = 0
for i in sayi:
    toplam += int(i)
print(toplam)
"""
"""

"""
"""
# a**2 + b**2 = c**2 ve a<b<c olan a+b+c=1000 olan abc sayı çarpımını bulun
def toplam_kontrol(a,b,c):
    if a + b+c == 1000:
        return 1
    return 0

def kare_kontrol(a,b,c):
    if c**2 == a**2 + b**2:
        return 1
    return 0

def anafonk():
    for i in range(1,1001):
        for j in range(1,1001):
            for k in range(1,1001):
                if toplam_kontrol(i,j,k) == 1 and kare_kontrol(i,j,k) and i<j<k:
                    print(i,j,k)
                    print(i*j*k)
"""

















