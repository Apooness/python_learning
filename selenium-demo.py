from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome()
url = "https://github.com"
driver.get(url)
time.sleep(0.5)
search = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/nav/ul/li[5]/a")
# time.sleep(0.5)
# search.send_keys("Python")
# time.sleep(0.5)
# search.send_keys(Keys.ENTER)
# time.sleep(0.5)
# repos = driver.find_elements_by_css_selector(".repo-list-item a.v-align-middle")
# for i in repos:
#     print(i.text)
# driver.close()
# print(dir(search))
search.click()