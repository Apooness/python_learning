"""
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# a = int(input("Bir sayı giriniz = "))
# if a > 0 and a < 100:
#     print("Sayı 0 ile 100 arasında")
# elif a > 100:
#     print("Sayı 100den büyük")
# else:
#     print("Sayı 0dan küçük")
"""
"""
#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#a = int(input("Bir sayı giriniz = "))
#if a > 0:
#    if a % 2 == 0:
#        print("Sayı pozitif çifttir")
#    else:
#        print("Sayı pozitif tektir")
#else:
#    print("Sayı Negatiftir")
"""
"""
#3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
#email = 'email@sadikturan.com'
#password = 'abc123'
#gemail = input("Email adresiniz = ")
#gpassword = input("Şifreniz = ")
#if email == gemail:
#    if password == gpassword:
#        print("Hoş geldiniz")
#    else:
#        print("Şifreniz yanlış")
#else:
#    print("Email adresi yanlış")
"""
"""
#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input("1. Sayı = "))
b = int(input("2. Sayı = "))
c = int(input("3. Sayı = "))

if a<b and a<c:
    if b<c:
        print(f"en küçük sayı {a}\nen büyük sayı {c}")
    else:
        print(f"en küçük sayı {a}\nen büyük sayı {b}")
elif b<c and b<a:
    if c<a:
        print(f"en küçük sayı {b}\nen büyük sayı {a}")
    else:
        print(f"en küçük sayı {b}\nen büyük sayı {c}")
else:
    if b<a:
        print(f"en küçük sayı {c}\nen büyük sayı {a}")
    else:
        print(f"en küçük sayı {c}\nen büyük sayı {b}")
"""
        

"""
#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#   b-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#   c-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = int(input("1. vize notu = "))
vize2 = int(input("2. vize notu = "))
final = int(input("final notu = "))
ort = (((vize1+vize2)/2) * 0.6) + (final * 0.4)
"""
"""
a)

if ort > 50:
    print("Geçtiniz")
else:
    print("Kaldınız")
"""
"""
b)

if ort >= 50:
    if final >= 50:
        print("Geçtiniz")
    else:
        print("Final notunuz yetersiz ")
        print("Kaldınız")
else:
    print("Ortalama yetersiz")
    print("Kaldınız")
"""
"""
c)

if ort>=50:
    print("Geçtiniz")
else:
    if final >=70:
        print("Final notunuz 70e eşit veya büyük olduğundan Geçtiniz")
    else:
        print("Kaldınız")
"""

"""
#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül: (Kilo / boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#   0-18.4    => Zayıf 
#   18.5-24.9 => Normal  
#   25.0-29.9 => Fazla Kilolu
#   30.0-34.9 => Şişman (Obez)

kilo = float(input("Kilonuz = "))
boy = float(input("Boyunuz = "))
index = kilo/(boy ** 2)

if index > 0 and index < 18.4:
    print(f"VKİniz = {index}\nZayıf")
elif index > 18.5 and index < 24.9:
    print(f"VKİniz = {index}\nNormal")
elif index > 25.0 and index < 29.9:
    print(f"VKİniz = {index}\nFazla Kilolu")
elif index > 30.0 and index < 34.9:
    print(f"VKİniz = {index}\nObez")
else:
    print("Yanlış girdi yaptınız")
""" 



