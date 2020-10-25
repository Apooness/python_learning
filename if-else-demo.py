# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 

#isim = input("İsminiz = ")
#yas = int(input("Yaşınız = "))
#egitim = input("Eğitim Düzeyi(küçük harflerle) = ")


#if yas >= 18:
#    if egitim == "lise" or egitim == "üniversite":
#        print("Ehliyet alabilirsiniz")
#    else:
#        print("Eğitim durumunuz yetersiz")
#else:
#    print("Büyüde gel")



# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# yazili1 = int(input("1. yazılı notu = "))
# yazili2 = int(input("2. yazılı notu = "))
# ort = (yazili1 + yazili2) / 2

# if ort <24:
#     print("Notunuz = 0")
# elif ort<44 and ort > 25:
#     print("Notunuz = 1")
# elif ort < 54 and ort > 45:
#     print("Notunuz = 2")
# elif ort < 69 and ort > 55:
#     print("Notunuz = 3")
# elif ort < 84 and ort > 70:
#     print("Notunuz = 4")
# else:
#     print("Notunuz = 5")





# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print('1.servis aralığı')
elif days>365 and days<=365*2:
    print('2.servis aralığı')
elif days>365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre.')
