import selenium
import pickle
from selenium import webdriver

link = "https://intel.ingress.com/intel"
ans = "n"

#open browser
driver = webdriver.Chrome()
driver.get(link)

#authorization
while ans != "y":
    ans = input("Are you authorized? (y/n)")
    if ans == "n":
        print("Authorize, bleat!")

#get cookies
pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))
driver.quit()

#open browser
driver = webdriver.Chrome()
driver.get(link)

#load cookies
driver.delete_all_cookies()
cookies = pickle.load(open("cookies.pkl","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

#test
driver.get(link)
input("pause")

driver.quit()
