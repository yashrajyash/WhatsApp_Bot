# Written by YASH
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://web.whatsapp.com/")

input('Scan QR code and hit enter <--|')
print('logged in........')
time.sleep(5)

message = 'This message is sent by whatsapp bot' + Keys.SHIFT + Keys.ENTER + 'please ignore this message'

contacts = pd.read_excel('contacts.xls', sheet_name='contacts')
names = contacts['Display Name'].tolist()

for name in names:

    search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)
    chat_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    chat_box.send_keys(message)
    chat_box.send_keys(Keys.ENTER)
    search_box.clear()
    time.sleep(2)

time.sleep(20)
driver.quit()