# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
#sayi = int(input("Bir sayı giriniz = "))
#sonuc = (sayi < 100) and (sayi > 0)
#print(sonuc)


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
#sayi = int(input("Bir sayı giriniz = "))
#sonuc = sayi > 0 and sayi % 2 == 0
#print(sonuc)


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
#aemail = 'email@sadikturan.com'
#apassword = 'abc123'

#gemail = input("Email adresiniz = ")
#gpassword = input("Şifrenizi giriniz = ")

#sonuc = (aemail == gemail) and (apassword == gpassword)
#print(sonuc)


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
#a = int(input("birinci sayıyı girin = "))
#b = int(input("birinci sayıyı girin = "))
#c = int(input("birinci sayıyı girin = "))

#sonuc = (a > b) and (a > c)
#print(sonuc)



# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
#vize1 = float(input("1. vize notu = "))
#vize2 = float(input("2. vize notu = "))
#final = float(input("final notu = "))
#sonuc = ortalama > 50 or ortalama == 50
#sonuc = ortalama >=50 and final > 50
#ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
#sonuc = ortalama >=50 or final >70
#print(sonuc)



# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


ad = input("Adınızı girin = ")
kilo = float(input("Kilonuzu giriniz = "))
boy = float(input("Boyunuzu giriniz = "))

ort = kilo / (boy ** 2)

zayif = ort <= 18.4
normal = ort >= 18.5 and ort <= 24.9
kilolu = ort >= 25.0 and ort <= 29.9
obez = ort >= 30.0 and ort <= 34.9

print(f'{ad} kilo indeksin: {ort} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{ad} kilo indeksin: {ort} ve kilo değerlendirmen normal: {normal}')
print(f'{ad} kilo indeksin: {ort} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{ad} kilo indeksin: {ort} ve kilo değerlendirmen obez: {obez}')

