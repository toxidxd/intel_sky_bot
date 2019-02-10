import selenium
import time
from selenium import webdriver


driver = webdriver.Chrome('/home/toxidxd/chromedriver')
driver.get("https://www.ingress.com/intel?ll=45.015035,39.087124&z=13")
driver.save_screenshot("./1.png")
#def setUp(self):
#        self.driver = webdriver.Firefox()

#driver = self.driver
#driver.get("http://www.python.org")






#https://www.ingress.com/intel?ll=45.015035,39.087124&z=13
