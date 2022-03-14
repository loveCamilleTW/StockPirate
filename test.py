import calendar
import pymysql
import requests

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from service import Service

db_settings = {
    "host": "127.0.0.1",
    "user": "loveCamilleTW",
    "password": "asdfasdf",
    "database": "stock",
    "charset": "utf8"
}

chrome = webdriver.Chrome(service=Service('./chromedriver'))
chrome.get("https://www.google.com.tw/")

try:
    WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='搜尋']")))
    input_block = chrome.find_element(By.XPATH,"//input[@aria-label='搜尋']")
    input_block.send_keys("中央大學")
    input_block.send_keys(Keys.ENTER)
    
except TimeoutException as e:
    print(e)    
# chrome.close()
