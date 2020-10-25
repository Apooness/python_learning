import math
sayi = int(input("Sayı Giriniz = "))
toplam = 0
liste = []
for i in range(1,sayi+1):
    liste.append(i)
toplam = (sayi + 1)/2 * len(liste)
toplam = int(toplam)
print(f"1'den girdiğiniz sayıya ({sayi}) kadar olan sayıların toplamı = {toplam} ")
print(f"1'den girdiğiniz sayıya ({sayi}) kadar olan sayıların çarpımı = {math.factorial(sayi)}")