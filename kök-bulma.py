def kok(a,b,c):
    delta = (b**2) - (4*a*c)
    x1 = (-b - delta**0.5)/(2*a)
    x2 = (-b + delta**0.5)/(2*a)
    if delta < 0:
        print("Gerçek Kök Yok")
    elif delta == 0:
        print("Birbirine eşit 2 kök var")
        print(f"{a}x2 + {b}x + {c} denkleminin kökleri = ")
        print(x1)
    else:
        print("2 Farklı kök vardır")
        print(f"{a}x2 + {b}x + {c} denkleminin kökleri = ")
        print(x1,x2,sep = "\n")
    
print("ax2 + bx + c şeklindeki denklemin katsayılarını giriniz")
a = int(input("x2nin katsayısı = "))
b = int(input("xin katsayısı = "))
c = int(input("sabti terim = "))
kok(a,b,c)

