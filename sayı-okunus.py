birler=[" ","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=[" ","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def sayı_okunus(sayi):
    birler_bas = sayi %10
    onlar_bas = sayi // 10
    return onlar[onlar_bas]+""+birler[birler_bas]

sayi = int(input("Sayi Giriniz = "))
print(f"Sayının Okunuşu = {sayı_okunus(sayi)}")
