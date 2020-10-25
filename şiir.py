with open("şiir.txt","r",encoding="utf-8") as file:
    yeni_liste =""
    liste = list()
    siir = file.read()
    kelimeler = siir.split("                    ")
    for i in kelimeler:
        i = i.strip("\n")
        liste.append(i)
    liste.remove("")
    for i in liste:
        yeni_liste += i[0]
print(yeni_liste)