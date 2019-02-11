
import selenium
import time
from selenium import webdriver
###
from selenium.webdriver.chrome.options import Options



#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--window-size=1920x1080')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--user-data-dir=/home/toxidxd/.config/google-chrome/')

link = "https://intel.ingress.com/intel"

driver = webdriver.Chrome()
driver.get(link)
#driver.get("https://www.ingress.com/intel?ll=45.015035,39.087124&z=13")
#driver.get("https://yandex.ru")
driver.save_screenshot("./1.png")

while link != "https://exit":
    link = "https://" + input("Input link or print exit: https://")
    driver.get(link)
    driver.save_screenshot("./2.png")

driver.quit()

#def setUp(self):
#        self.driver = webdriver.Firefox()

#driver = self.driver
#driver.get("http://www.python.org")






#https://www.ingress.com/intel?ll=45.015035,39.087124&z=13
