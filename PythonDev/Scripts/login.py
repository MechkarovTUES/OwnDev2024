import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pyautogui
import time

url = "https://monkeytype.com/login"
driver = webdriver.Chrome()

driver.get(url)
username = "alexandar.im@gmail.com"
password = "sekfer-9ricpa-Timfyz"

# Define a custom expected condition to wait for an element to be present and clickable
def presence_and_clickability_of_element(locator):
    return EC.presence_of_element_located(locator) and EC.element_to_be_clickable(locator)

# Use WebDriverWait with the custom condition
username_locator = (By.XPATH, '//*[@id="pageLogin"]/div[3]/form/input[1]')
username_input = WebDriverWait(driver, 10).until(presence_and_clickability_of_element(username_locator))

driver.execute_script("arguments[0].scrollIntoView();", username_input)
username_input.send_keys(username)

password_locator = (By.XPATH, '//*[@id="pageLogin"]/div[3]/form/input[2]')
password_input = WebDriverWait(driver, 10).until(presence_and_clickability_of_element(password_locator))

driver.execute_script("arguments[0].scrollIntoView();", password_input)
password_input.send_keys(password)

login_button_locator = (By.XPATH, '//*[@id="pageLogin"]/div[3]/form/button[1]')
login_button = WebDriverWait(driver, 10).until(presence_and_clickability_of_element(login_button_locator))

driver.execute_script("arguments[0].scrollIntoView();", login_button)
login_button.click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

error_message = "Incorrect username or password."

errors_locator = (By.CSS_SELECTOR, ".flash-error")
errors = WebDriverWait(driver, 10).until(presence_and_clickability_of_element(errors_locator))

if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

# time.sleep(10)
driver.quit()
