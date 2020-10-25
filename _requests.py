import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="
bozulan_birim = input("Bozdurulan Birim = ")
alinan_birim = input("Alınan Birim = ")
miktar = int(input(f"Ne kadar {bozulan_birim} bozdurmak istiyorsunuz = "))


result = requests.get(api_url+bozulan_birim)
result = json.loads(result.text)
print("1 {0} = {1} {2}".format(bozulan_birim,result["rates"][alinan_birim],alinan_birim))
alinan_miktar = miktar*result["rates"][alinan_birim]
print(f"Almanız Gereken miktar = {alinan_miktar} {alinan_birim}")





"""
result = requests.get("https://jsonplaceholder.typicode.com/users")
result = json.loads(result.text)
for i in result:
    if i["id"] == 1:
        # print(i)
        adress = i["address"]
        print("name =", i["name"],"\n" ,"streets = ",adress["street"],"\n","phone number = ",i["phone"])

"""