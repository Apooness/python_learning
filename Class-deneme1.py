"""
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi):
        print("Kitabınız Oluşturuluyor!!!")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
    def __str__(self):
        return f"Kitabın ismi: {self.isim}\nKitabın Yazarı: {self.yazar}\nSayfa Sayısı: {self.sayfa_sayisi}"
    def __len__(self):
        return self.sayfa_sayisi
kitap1 = Kitap("Piramit","William Golding",223)
print(kitap1)
print("Kitabınız Oluşturuldu!!!")
"""
"""
class Futbolcu():
    def __init__(self,ad,soyad,mevki,yas,takim,maas):
        self.ad = ad
        self.soyad = soyad
        self.mevki = mevki
        self.yas = yas
        self.takim = takim
        self.maas = maas
    def mevki_oğren(self,yeni_mevki):
        self.mevki.append(yeni_mevki)
    def Bilgiler(self):
        for i in self.mevki:
            self.mevki = i
        print(f"
        Futbolcunun Bilgileri;
        Adı:{self.ad}
        Soyadı:{self.soyad}
        Takımı:{self.takim}
        Mevkisi:{self.mevki}
        Maaşı:{self.maas}
        ")
    def maas_arttir(self,zam_miktari):
        self.maas += zam_miktari
futbolcu1 = Futbolcu("Rıdvan","Yılmaz",["Sol Bek"],"19","Beşiktaş",50000)
futbolcu1.maas_arttir(50000)
# futbolcu1.mevki_oğren("Sol Kanat")
futbolcu1.Bilgiler()
"""
"""
class Ulkemiz():
    def __init__(self,ulke_adi,sehir_adi,plaka_kodu,bolge):
        self.ulke_adi = ulke_adi
        self.sehir_adi = sehir_adi
        self.plaka_kodu = plaka_kodu
        self.bolge = bolge
    def yazdir(self):
        print(f"Şehirin:
Bulunduğu ülke: {self.ulke_adi}
Adı: {self.sehir_adi}
Plaka Kodu: {self.plaka_kodu}
Bulunduğu Bölge = {self.bolge}")
sehir1 = Ulkemiz("Türkiye","Aydın",9,"Ege Bölgesi")
sehir1.yazdir()
"""







