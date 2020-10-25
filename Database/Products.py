import mysql.connector

def insertProduct(name,price,ImageUrl,description):
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,ImageUrl,description) VALUES (%s,%s,%s,%s)"
    Values = (name,price,ImageUrl,description)

    cursor.execute(sql,Values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"hata:{err}")
    finally:
        connection.close()
        print("Database ile ilişki sonlandırılıyor")

def insertProducts(liste):
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,ImageUrl,description) VALUES (%s,%s,%s,%s)"
    Values = liste

    cursor.executemany(sql,Values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"hata:{err}")
    finally:
        connection.close()
        print("Database ile ilişki sonlandırılıyor")

# secim = int(input("Görmek istediğiniz telefonun idsi: "))
# liste = []
# while True:
#     name = input("ürün adı:")
#     price = float(input("ürün fiyatı:"))
#     ImageUrl = input("ürün resim adı:")
#     description = input("ürün açıklaması:")
#     liste.append((name,price,ImageUrl,description))
#     secim = input("Kayıt eklemek ister misiniz(e/h): ")
#     if secim == "h":
#         insertProducts(liste)
#         break

def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()
    # sql = "Select * From products"
    # sql = "Select * From categories"
    # sql = "Select * From products inner join categories on categories.id = products.categoryid"
    sql = "Select products.name,products.price,categories.name From products inner join categories on categories.id = products.categoryid"

    cursor.execute(sql)
    result = cursor.fetchall()
    # result = cursor.fetchmany(3)
    # result = cursor.fetchone()
    # print(f"telefon adı: {result[0].ljust(20)} fiyatı:{str(result[1]).ljust(20)} açıklaması: {result[2]}")

    for i in result:
        print(i)
        # print(f"telefon idsi:{str(i[0]).ljust(5)}telefon adı: {i[1].ljust(20)} fiyatı:{str(i[2]).ljust(20)}")
        # print(f"telefon adı: {i[1].ljust(20)} fiyatı: {i[2]} açıklaması:{i[4]}")
# getProducts()

def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()
    sql = "Select * From products Where id=%s"
    param = (id,)
    cursor.execute(sql,param)

    result = cursor.fetchone()
    print(f"telefon idsi:{str(result[0]).ljust(5)}telefon adı: {result[1].ljust(20)} fiyatı:{str(result[2]).ljust(20)}")
# getProductById(secim)

def getProductInfo():
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()
    # sql = "Select Count(name) From products"
    # sql = "Select Avg(price) From products"
    # sql = "Select MIN(price) From products"
    # sql = "Select MAX(price) From products"
    # sql = "Select SUM(price) From products"
    sql = "Select name,price from products Where price = (Select MAX(price) From products)"

    cursor.execute(sql)
    result = cursor.fetchone()
    print(f"Telefon: {result[0]} {result[1]} ")
# getProductInfo()
    
def UpdateProduct(id,name,price):
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()
    if name != '':
        sql = "Update products Set name = %s, price = %s where id = %s"
        values = (name,price,id)
        cursor.execute(sql,values)
        connection.commit()

    else:
        sql = "Update products Set price = %s where id = %s"
        values = (price,id)
        cursor.execute(sql,values)
        connection.commit()
# id = int(input("değiştirmek istediğin telefonun idsi: "))
# name = input("değiştirmek istediğin telefonun yeni adı: ")
# price = int(input("değiştirmek istediğin telefonun yeni fiyatı: "))
# UpdateProduct(id,name,price)

def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="deneme1")
    cursor = connection.cursor()
    sql = "Delete from products where id = %s"
    values = (id,)
    cursor.execute(sql,values)
    connection.commit()
# id = int(input("Silmek istediğin telefonun idsi: "))
# deleteProduct(id)
