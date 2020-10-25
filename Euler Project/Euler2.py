# 4 milyonu geçmeyen butun cift fibonacci sayilarinin toplamı
fib1 = 1
fib2 = 2
temp = 0
toplam = 0

while fib1<4000000:
        temp = fib2
        fib2 += fib1

        if fib1 % 2 == 0:
            toplam += fib1
        fib1 = temp
print(toplam)
print(temp)