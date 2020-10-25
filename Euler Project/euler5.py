# 1 den 20 e kadar bütün sayılara bölünen en küçük sayı
def bolunur(sayi):
    for i in range(1,21):
        if sayi % i != 0:
            return 0
    return 1
sayi = 1
while bolunur(sayi) != 1:
    sayi +=1
print(sayi)