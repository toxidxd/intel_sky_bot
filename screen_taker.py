
import selenium
import time
import pickle
from selenium import webdriver
###
#from selenium.webdriver.chrome.options import Options


link = "https://intel.ingress.com/intel"

driver = webdriver.Chrome()
time.sleep(30)
driver.get(link)

driver.delete_all_cookies()
cookies = pickle.load(open("cookies.pkl","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get(link)

while link != "https://exit":
    link = "https://" + input("Input link or print exit: https://")
    driver.get(link)
    time.sleep(30)
    driver.save_screenshot("./2.png")

driver.quit()
