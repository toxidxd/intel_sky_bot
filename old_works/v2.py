#https://www.ingress.com/intel?ll=45.015035,39.087124&z=13

import selenium
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

executable_path = '/home/toxidxd/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-data-dir=/home/toxidxd/.config/google-chrome/')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
#driver.maximize_window()


#driver.get("https://www.ingress.com/intel?ll=45.015035,39.087124&z=13")
driver.get("https://www.google.com")
driver.save_screenshot('screenselch.png')
driver.quit()
