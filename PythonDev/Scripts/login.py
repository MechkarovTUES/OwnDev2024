import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pyautogui
import time


url = "https://monkeytype.com/login"
driver = webdriver.Chrome()  # You can use other drivers like Firefox or Edge


driver.get(url)
username = "alexandar.im@gmail.com"
password = "sekfer-9ricpa-Timfyz"
# find username/email field and send the username itself to the input field
driver.find_element("xpath", '//*[@id="pageLogin"]/div[3]/form/input[1]').send_keys(username)
# find password input field and insert password as well
driver.find_element("xpath", '//*[@id="pageLogin"]/div[3]/form/input[2]').send_keys(password)
# click login button
driver.find_element("xpath", '//*[@id="pageLogin"]/div[3]/form/button[1]').click()
# wait the ready state to be complete


WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

time.sleep(10)
driver.quit()