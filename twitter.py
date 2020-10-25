from twitterUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
word = input("Aramak istediğiniz kelime: ")

class Twitter():
    def __init__(self,username,password):
        self.browserprofile = webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver.exe",chrome_options=self.browserprofile)
        self.username = username
        self.password = password

    def signin(self):
        self.browser.get("https://twitter.com/login")
        self.browser.maximize_window()
        time.sleep(2)

        usernameinput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        passwordinput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)
        passwordinput.send_keys(Keys.ENTER)
        time.sleep(2)

    def search(self,word):
        searchinput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        searchinput.send_keys(word)
        time.sleep(2)
        searchinput.send_keys(Keys.ENTER)
        time.sleep(5)
        
        results = []

        liste = self.browser.find_elements_by_xpath("//div[@data-testid = 'tweet']/div[2]/div[2]/div[1]")
        time.sleep(2)
        print("count = "+str(len(liste)))
        for i in liste:
            results.append(i.text)


        loopcounter = 0
        lastheight = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopcounter > 3 :
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(4)
            newheight = self.browser.execute_script("return document.documentElement.scrollHeight")
            if lastheight == newheight:
                break
            lastheight = newheight
            loopcounter += 1

            liste = self.browser.find_elements_by_xpath("//div[@data-testid = 'tweet']/div[2]/div[2]/div[1]")
            time.sleep(2)
            print("count = "+str(len(liste)))
            for i in liste:
                results.append(i.text)
        count = 1
        with open("tweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f'{count}-{item}+\n')
                count +=1

twitter = Twitter(username,password)
twitter.signin()
twitter.search(word)
