from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url = "https://music.youtube.com/"
driver.get(url)
time.sleep(0.5)
explore = driver.find_element_by_xpath('//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-pivot-bar-renderer/ytmusic-pivot-bar-item-renderer[2]/yt-formatted-string')
explore.click()
time.sleep(2)
categoriesscreen = driver.find_elements_by_xpath('//*[@id="text"]')
categoriesscreen = categoriesscreen[1]
categoriesscreen.click()
time.sleep(3)
categories = driver.find_elements_by_css_selector("#items > ytmusic-navigation-button-renderer")
for i in categories:
    print("Dinleyebileceğiniz Kategoriler: ",i.text)


# my_category = driver.find_element_by_css_selector(f"#items > ytmusic-navigation-button-renderer:nth-child{sayi} > button")
# my_category.click()
# time.sleep(1)
# playlist = driver.find_element_by_xpath('//*[@id="items"]/ytmusic-two-row-item-renderer[1]/a')
# playlist.click()
# time.sleep(1)
driver.close()