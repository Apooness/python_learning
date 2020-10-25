from instagramUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,username,password):
        self.browserprofile = webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option("prefs",{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signin(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(2)

        usernameinput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordinput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)
        passwordinput.send_keys(Keys.ENTER)
        time.sleep(3)

    def getFollows(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(2)
        
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break
        
        followers = dialog.find_elements_by_css_selector("li")

        followerList = []

        for user in followers:
            link = user.find_element_by_css_selector("a").text
            followerList.append(link)            


        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
            
        

        




instagram = Instagram(username,password)
instagram.signin()
instagram.getFollows()
