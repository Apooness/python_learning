def pisagor():
    pisagorlist = list()
    i = int(input("Küçük sayı = "))
    j = int(input("Büyük sayı = "))
    for a in range(i,j+1):
        for b in range(i,j+1):
            c = (a**2 + b**2) ** 0.5

            if (c == int(c)):
                pisagorlist.append((a,b,int(c)))

    return pisagorlist

for i in pisagor():
    print(i)