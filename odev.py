"""
# 16 - kullanıcının girecek olduğu iki sayı arasında ki asal sayıları yazdıran programı yazınız 
# 17 – a = 5.34-2.03 b = 4.23-1.02 Yukarıda verilen a ve b değişkenlerinin eşitliğini kontrol ediniz Eğer eşit değillerse nedenini araştırınız 
"""
# 1- Kullanıcıdan bir sayı alarak ekrana basan programı yazınız. 
# print(int(input("Bir sayı giriniz = ")))
 
# 2- Kullanıcıdan string alarak ekrana yazan programı yazınız. 
# print(input("Bir veri giriniz = "))

# 3- Kullanıcıdan iki sayı alarak toplamını, farkını, çarpımını ve bölümünü bulan programı yazınız.  
# a = int(input("1. sayı = "))
# b = int(input("2. sayı = "))
# print(a+b,a/b,a*b,a-b)

# 4- Kullanıcı tarafından girilen iki sayının ortalamasını bulan programı yazınız. 
# a = int(input("1. sayı = "))
# b = int(input("2. sayı = "))
# print((a+b)/2)

# 5- girilen vize ve final notuna göre vizenin yüzde 30 unu finalin yüzde 70 ini alarak hesaplayan ve ekrana basan programı yazınız. 
# a = int(input("vize = "))
# b = int(input("final = "))
# print((a*0.3) + (b*0.7))

# 6- kullanıcıdan boy ve kilo bilgisi alarak vücut kitle indexini hesaplayan programı yazınız. (kilo/boy * boy)(boy 1.70 şeklinde girilmelidir.) 
# a = float(input("boy(boy 1.70 şeklinde girilmelidir.) = "))
# b = int(input("kilo = "))
# print(b/(a*a))

# 7- Kullanıcının girdiği iki sayının yerlerini değiştiren programı yazınız. (x değeri ve y değeri alınarak içerikleri değiştirilmeli) 
# a = int(input("1. sayı = "))
# b = int(input("2. sayı = "))
# a,b = b,a
# print(a,b)

# 8- Taban ve yükseklik değeri girilen üçgenin alanını hesaplayan programı yazınız. 
# a = int(input("taban = "))
# b = int(input("yükseklik = "))
# print((a*b)/2)

# 9- Kullanıcıdan gerilim ve direnç değeri alarak akım değeri hesaplayan ve ekrana yazan programı  
# V = i*R
# a = int(input("gerilim = "))
# b = int(input("direnç = "))
# print("akım = ",a/b)

# 10 – kullanıcıdan adını ve yaşını alarak , adını yaşı kadar yazdıran programı yazınız. 
# a = input("ad = ")
# b = int(input("yaş = "))
# print(a*b)

# 11- kullanıcının girecek olduğu 10(on) sayının toplamını ve bu sayıların ortalamasını bularak ekrana yazdıran programı yazınız. 
# sayac = 0
# toplam = 0
# while sayac < 10:
#     a = int(input("sayı giriniz = "))
#     toplam += a
#     sayac +=1
# print(toplam)

# 12- 0 ile yüz arasında kullanıcının sayılar girmesini ve 0’dan küçük 100’den büyük sayı girmesi durumunda girilmiş tüm sayıların toplamını yazdıran programı yazınız. 
# toplam = 0
# while True:
#     a = int(input("Sayı giriniz = "))
#     if a < 0 or a > 100:
#         print(toplam)
#         break
#     toplam += a

# 13 – Bir turnuva düzenleyerek, turnuvaya katılım şartlarını kişilere sorarak turnuvaya katılıp katılamayacaklarını yazdıran programı yazınız. 
# okul = input("okul düzeyi(i/o/l) = ")
# bilgi = input("Satranç biliyor musunuz(e/h) = ")
# if okul == "o" and bilgi == "e":
#     print("Turnuvaya katılabilirsiniz.")
# else:
#     print("Koşulları sağlamıyorsunuz!!!")
 
# 14- 100 kişilik bir ekipten yukarıda ki hazırlanacak turnuvaya kaç kişinin katılıp kaç kişinin katılamayacak olduğunu yazdıran programı yazınız. 
# katilim = 0
# for i in range(0,4):
#     okul = input("okul düzeyi(i/o/l) = ")
#     bilgi = input("Satranç biliyor musunuz(e/h) = ")
#     if okul == "o" and bilgi == "e":
#         print("Turnuvaya katılabilirsiniz.")
#         katilim+=1
#     else:
#         print("Koşulları sağlamıyorsunuz!!!")
# print(f"Turnuvaya {katilim} kişi katılabilir")

# 15- 50 kişinin yukarıda ki turnuvaya katılması için toplam ne kadar başvuru olduğunu ekrana yazdıran programı yazınız. 

