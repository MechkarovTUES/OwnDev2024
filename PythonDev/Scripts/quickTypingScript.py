import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pyautogui
import time


url = "https://monkeytype.com"
driver = webdriver.Chrome()  # You can use other drivers like Firefox or Edge


driver.get(url)



response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

# Find the div with id="words"
div_words = soup.find('div', id='words')

def ScrapWords():
    div_words = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "words")))
    return div_words.text


# Wait for the div with id="words" to be present in the DOM
time.sleep(10)
try:
    start_time = time.time()
    '''while time.time() - start_time < 30:  # Continue loop until 30 seconds have passed
        words_str = ScrapWords()
        words_list = words_str.split()
        print(words_list)
        for word in words_list:
            if word != 'correct':
                pyautogui.write(word + ' ')
            time.sleep(0.1)  # Adjust the sleep time as needed'''
    words_str = ScrapWords()
    words_list = words_str.split()
    print(words_list)
    for word in words_list:
        if word != 'correct':
            pyautogui.write(word + ' ')
        time.sleep(0.005)
    time.sleep(60)
finally:
    driver.quit()