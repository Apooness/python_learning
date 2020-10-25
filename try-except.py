"""
ay = 12
try:
    yas = int(input("Yaşınız = "))
except Exception as ex:
    print("Hata Oluştu")

print(str(ay*yas)+" ay yaşamışsınız.")
"""
"""
try:
    sayi1 = int(input("1. Sayı = "))
    sayi2 = int(input("2. Sayı = "))

    if sayi2 == 0:
        raise Exception("2. Sayı 0 rakamını Alamaz!!!")

    print("sayi1"," + ","sayi2", " = ",(sayi1+sayi2))
except Exception as hata:
    print("Hata var. Hatanız = ",hata)
else:
    try:
        print("sayi1 / sayi2 = ",sayi1/sayi2)
    except ZeroDivisionError as hata:
        print("Hatanız Var. Hatanız = ",hata)
"""
password = input("Şifreniz = ")

def sayikontrol(metin):
    for i in metin:
        if i.isnumeric():
            return False
    return True

def uzunlukkontrol(metin):
    adim = "Uzunluk Fonksiyonu"
    if len(metin) < 8:
        return True
    else:
        return False

def buyukkontrol(metin):
    for i in metin:
        if i.isalpha():
            if i.supper():
                return False
    return True

def sifrekontrol(metin):
    try:
        adim = "A1_1"
        password = input("Şifreniz = ")
        adim = "A2"
        if sayikontrol(password):
            raise Exception("Şifrenizde Numara Bulunmalıdır!!!")
        if uzunlukkontrol(password):
            raise Exception("Şifreniz En az 8 karakter olmalıdır!!!")
        if buyukkontrol(password):
            raise Exception("Şifrenizde En az 1 Büyük harf olmalıdır!!!")
        return True

    except Exception as hata:
        print(hata)
        return False






