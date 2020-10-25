""" AŞAMA 1
sesli_harf = "aeıioöuüAEIİOÖUÜ"
sayac = 0
kelime = input("Kelime Giriniz = ")
for i in kelime:
    if i in sesli_harf:
        sayac +=1
print(f"{kelime} kelimesinin içinde {sayac} tane sesli harf vardır")
"""
""" AŞAMA 2
sesli_harf = "aeıioöuüAEIİOÖUÜ"
sayac = 0
kelime = input("Kelime veya Cümle Giriniz = ")

def sesli(harf):
    if harf in sesli_harf:
        print("Gönderilen harf ",harf)
        return harf in sesli_harf
def arttir(sayac):
    for harf in kelime:
        if sesli(harf):
            sayac +=1
    return sayac
print(f"{kelime} kelimesinin içinde {arttir(sayac)} tane sesli harf vardır")
"""
"""AŞAMA 3
sesli_harf = "aeıioöuüAEIİOÖUÜ"
sayac = 0
def kelimeal():
    return input("Kelime veya Cümle Giriniz = ")

def sesli(harf):
    if harf in sesli_harf:
        print("Gönderilen harf ",harf)
        return harf in sesli_harf
    
def arttir(sayac,kelime):
    for harf in kelime:
        if sesli(harf):
            sayac +=1
    return sayac

def yazdir(kelime):
    print(f"{kelime} kelimesinin içinde {arttir(sayac,kelime)} tane sesli harf vardır")
def calistir():
    kelime = kelimeal()
    yazdir(kelime)
calistir()
"""
"""AŞAMA 4
class HarfSayac():
    def __init__(self):
        self.sesli_harf = "aeıioöuü"
        self.sessiz_harf = "bmnvcxzsqwdrftgyhjklpğşç"
        self.bosluk = " "
        self.seslisayac = 0
        self.sessizsayac = 0
        self.bosluksayac = 0
    def kelimeal(self):
        alinan_kelime = input("Kelime veya Cümle Giriniz = ")
        alinan_kelime = alinan_kelime.lower()
        return alinan_kelime
    def seslidir(self,harf):
        print("Gönderilen harf",harf)
        return harf in self.sesli_harf

    def sessizdir(self,harf):
        return harf in self.sessiz_harf

    def bosluk(self,harf):
        return harf in self.bosluk

    def arttir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.seslisayac +=1
            elif self.sessizdir(harf):
                self.sessizsayac +=1
            else:
                self.bosluksayac +=1
        return self.seslisayac,self.sessizsayac

    def yazdir(self):
        sesli,sessiz = self.arttir()
        print(f"{self.kelime} kelimesinin içinde
                  {self.seslisayac} tane sesli harf
                  {self.sessizsayac} tane sessiz harf
                  {self.bosluksayac} tane boşluk
                  vardır")
    def calistir(self):
        self.kelime = self.kelimeal()
        self.yazdir()

if __name__ == "__main__":
    sayac = HarfSayac()
    sayac.calistir()
"""
"""
class HarfSayaci():
    def __init__(self):
        self.harf_seti = ""
        self.sayac = 0
        self.ifade = ""

    def kelimeal(self):
        alinankelime = input("Kelime veya Cümle Giriniz = ")
        alinankelime = alinankelime.lower()
        return alinankelime

    def kontrol(self,harf):
        return harf in self.harf_seti
        print("Gönderilen harf: ",harf)

    def arttir(self):
        for harf in self.kelime:
            if self.kontrol(harf):
                self.sayac +=1
        return self.sayac

    def yazdir(self):
        sayi = self.arttir()
        print("{self.kelime}
                 {sayi} {self.ifade} harf var.")

    def calistir(self):
        self.kelime = self.kelimeal()
        self.yazdir()

class SesliHarf(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.harf_seti = "aeoöüuiı"
        self.ifade = "Sesli"

class SessizHarf(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.harf_seti = "szxwqrdfcvgtbnhyjmklpğçş"
        self.ifade = "Sessiz"

class Bosluk(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.harf_seti = " "
        self.ifade = "Boşluk"

class GenelKontrol(HarfSayaci):
    def __init__(self):
        super().__init__()
        self.kontrol1 = SesliHarf()
        self.kontrol2 = SessizHarf()
        self.kontrol3 = Bosluk()

    def yazdir(self):
        self.kontrol1.kelime = self.kelime
        self.kontrol2.kelime = self.kelime
        self.kontrol3.kelime = self.kelime
        sesli,sessiz,bosluk = self.kontrol1.arttir(),self.kontrol2.arttir(),self.kontrol3.arttir()

        print(f"{self.kelime} kelimesinin içinde
                 {sesli} tane sesli
                 {sessiz} tane sessiz
                 {bosluk} tane boşluk
                 vardır...
                 ")

if __name__ == "__main__":
    sayac = GenelKontrol()
    sayac.calistir()
"""

class Calisan():
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
    def maasarttir(self,zam_miktari):
        self.maas += zam_miktari
        return self.maas
    def maaszam(self,zam_orani):
        self.maas = self.maas + ((self.maas*zam_orani)/100)

class Yazilimci(Calisan):
    def __init__(self, ad, soyad, maas, dil):
        super().__init__(ad, soyad, maas)
        self.dil = dil
    def yazdir(self):
            print(f"{self.ad} {self.soyad} isimli yazılımcının maaşı = {self.maas} ve ilgilendiği dil = {self.dil}")
    def maasarttir(self,zam_miktari):
        self.maas += zam_miktari
        return self.maas    
    def maaszam(self,zam_orani):
        self.maas = self.maas + ((self.maas*zam_orani)/100)
        return self.maas

class Donanimci(Calisan):
    def __init__(self, ad, soyad, maas, donanim):
        super().__init__(ad, soyad, maas)
        self.donanim = donanim
    def yazdir(self):
        print(f"{self.ad} {self.soyad} isimli donanımcının maaşı = {self.maas} ve ilgilendiği donanım = {self.donanim}")

soru = 0
secim = input("Göreviniz(1- Yazılım)(2- Donanım) =  ")
if secim == "1":
    ad = input("Adınız = ")
    soyad = input("Soyadınız = ")
    maas = int(input("Maaşınız = "))
    dil = input("Bildiğiniz dil = ")
    yaz1 = Yazilimci(ad,soyad,maas,dil)    
    soru = input("Yapmak istediğiniz işlem(1- maaş arttır)(q- çıkış) = ")
    while True:
        if soru == "q":
            print("çıkış yapılıyor...")
            break
        elif soru == "1":
            zam = input("Zam oranını nasıl girmek istersiniz(1- yüzde)(2- maaş arttır) =  ")
            if zam == "1":
                zam_orani = int(input("Maaşınıza Yapılacak zam oranı = "))
                maas = Yazilimci.maaszam(zam_orani)
            else:
                zam_miktari = int(input("Maaşınıza yapılacak zam miktarı = "))
                maas = Yazilimci.maasarttir(zam_miktari) 
                
    yaz1.yazdir()
elif secim == "2":
    ad = input("Adınız = ")
    soyad = input("Soyadınız = ")
    maas = int(input("Maaşınız = "))
    donanim = input("İlgilendiğiniz Donanım = ")    
    don1 = Donanimci(ad,soyad,maas,donanim)    
    don1.yazdir()
else:
    print("Hatalı Görev Seçimi")
# yaz1 = Yazilimci(yazilimad,yazilimsoyad,yazilimmaas,yazilimdil)
# yaz1.yazdir()







