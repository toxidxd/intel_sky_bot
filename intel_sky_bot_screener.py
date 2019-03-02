import logging
import selenium
import time
import pickle
from selenium import webdriver
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)





print("Hello, shit!")
##################
driver = webdriver.Chrome()
driver.get("https://intel.ingress.com/intel")
driver.delete_all_cookies()
cookies = pickle.load(open("cookies.pkl","rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://intel.ingress.com/intel")
print("Bot initialized")
#################

x = 0

while x == 0:
	name = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
	name = name + ".png"
	link = "https://intel.ingress.com/intel?ll=46.848378,40.304031&z=15"
	driver.get(link)
	time.sleep(10)
	driver.save_screenshot(name)
	time.sleep(50)
