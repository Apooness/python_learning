import requests        
class Github():
    def __init__(self):
        self.api_url = "https://api.github.com/users/"
    def userinfo(self,username):
        response = requests.get(self.api_url+username)
        return response.json()
    def repository(self,username):
        response = requests.get(self.api_url+username+"/repos")
        return response.json()
github = Github()
while True:
    secim = input("1- User info\n2- Repositories\n3- Exit\nChoices = ")
    if secim == "3":
        print("çıkılıyor!!!")
        break
    else:
        if secim == "1":
            username = input("Username = ")
            result = github.userinfo(username)
            print(f"name: {result['name']} blog: {result['blog']} bio: {result['bio']}")
        elif secim == "2":
            username = input("USername = ")
            result = github.repository(username)
            for i in result:
                print(i["name"])