x = []
sayi1 = int(input("Küçük sayı = "))
sayi2 = int(input("Büyük sayı = "))

for a in range(sayi1,sayi2+1):
    t = 0
    for i in range(1,a):
        if a % i == 0:
            t+=i
    if t ==a:
        x.append(a)

print(f"{sayi1} ile {sayi2} arasında {len(x)} tane sayı vardır.")
print(f"Bu sayılar = {x}")