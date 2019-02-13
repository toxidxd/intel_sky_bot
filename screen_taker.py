
import selenium
import time
import pickle
from selenium import webdriver
###
#from selenium.webdriver.chrome.options import Options

#https://intel.ingress.com/intel?ll=46.848378,40.304031&z=15
link = "https://intel.ingress.com/intel"

driver = webdriver.Chrome()

driver.get(link)

driver.delete_all_cookies()
cookies = pickle.load(open("cookies.pkl","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get(link)

while link != "https://exit":
    link = "https://" + input("Input link or print exit: https://")
    if link != "https://exit":
        driver.get(link)
        time.sleep(15)
        driver.save_screenshot("./2.png")

driver.quit()
