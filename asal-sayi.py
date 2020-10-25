sayi = int(input("Sayı = "))
asalmi = True

if sayi == 1:
    asalmi = False
    
for i in range(2,sayi):
    if sayi %i ==0:
        i+=1
        asalmi = False
        break
    else:
        asalmi = True
        
if asalmi == True:
    print("Sayı Asal")
else:
    print("sayı asal değil")