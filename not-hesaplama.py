kalanlar = []
gecenler = []
def not_hesapla(n):
    n = n[:-1]
    liste = n.split(",")
    ad = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])
    ort = (vize1*0.3) + (vize2*0.3) + (final*0.4)
    if ort >= 90:
        harf = "AA"
    elif ort >= 85:
        harf = "BA"
    elif ort >= 80:
        harf = "BB"
    elif ort >= 75:
        harf = "CB"
    elif ort >= 70:
        harf = "CC"
    elif ort >= 65:
        harf = "DC"
    elif ort >= 60:
        harf = "DD"
    elif ort >= 55:
        harf = "FD"
    else:
        harf = "FF"
    if harf == "FF" or harf == "FD" or harf == "DD" or harf == "DC":
        return kalanlar.append(ad + " 'KALDINIZ': " +  harf + "\n")
    else:
        return gecenler.append(ad + " 'GEÇTİNİZ': " + harf + "\n")
        
with open("Not_Dosyası","r",encoding="utf-8") as file:
    for i in file:
        not_hesapla(i)
    with open("Kalanlar","w",encoding="utf-8") as file2:
        for i in kalanlar:
            file2.write(i)
    with open("Geçenler","w",encoding="utf-8") as file3:
        for i in gecenler:
            file3.write(i)