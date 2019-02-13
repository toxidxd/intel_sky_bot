import logging
import selenium
import time
import pickle
from selenium import webdriver
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token='465106047:AAGzJs9aO5QXxt2QGBfNQgcdxjsrVAvJMKI') # Токен API к Telegram
dispatcher = updater.dispatcher

print("Hello, shit!")

def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="ne starT")
    file = open("1.png", 'rb')
    bot.send_photo(chat_id=update.message.chat_id, photo=file)

def give_screen(bot, update):
    link = "https://intel.ingress.com/intel?ll=46.848378,40.304031&z=15"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.delete_all_cookies()
    cookies = pickle.load(open("cookies.pkl","rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(link)
    #time.sleep(15)
    driver.save_screenshot("./screen.png")
    driver.quit()
    scr = open("screen.png", "rb")
    bot.send_message(chat_id=update.message.chat_id, text="na tebe screeeen")
    bot.send_photo(chat_id=update.message.chat_id, photo=scr)


# Хендлеры
start_command_handler = CommandHandler('start', start_command)
give_screen_command_handler = CommandHandler('musiclist', give_screen)


# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(give_screen_command_handler)







# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
