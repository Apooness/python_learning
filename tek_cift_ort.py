sayilar = [1, 2, 3, 4, 34, 62, 63, 32, 100, 105]
def wrapper(sayilar):
    cift_toplam = 0
    cift_adet = 0
    tek_toplam = 0
    tek_adet = 0
    tek_ort = 0
    cift_ort = 0
    

    for sayi in sayilar:
        if sayi % 2 == 0:
            cift_toplam = cift_toplam + sayi
            cift_adet +=1
        else:
            tek_toplam = tek_toplam + sayi
            tek_adet += 1
            
    tek_ort = tek_toplam/tek_adet
    cift_ort = cift_toplam/cift_adet
    print(f"Teklerin Toplamı = {tek_toplam}")
    print(f"Teklerin Ortalaması = {tek_ort}")
    print(f"Çiftlerin Toplamı = {cift_toplam}")
    print(f"Çiftlerin Ortalaması = {cift_ort}")


wrapper(sayilar)








