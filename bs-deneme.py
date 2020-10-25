from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="brother" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="step bro" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser")
# with open("index.html",encoding="UTF-8") as fp:
#     soup = BeautifulSoup(fp,"html.parser")
# result = soup
# # soup.head.name = "Deneme"
# # result = result.name
# soup.h1["id"] = "Başlık"
# result = soup.h1["id"]
# result = result.attrs
# result = soup.findAll("a")
# for i in result:
#     # i = i["class"]
#     print(i["class"])
# result = soup.p
# print(result)

for string in soup.stripped_strings:
    print(repr(string))
    



