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




# Wait for the div with id="words" to be present in the DOM
try:
    div_words = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "words"))
    )
    
    # Extract and print the content of the div
    print(div_words.text)
    '''
    if div_words:
    # Extract letters from each word
        words = div_words.find_all('div', class_='word')
    
        for word in words:
            letters = word.find_all('letter')
            word_text = ''.join(letter.text for letter in letters)
            print(word_text)
        else:
            print("Div with id='words' not found.")
        '''
finally:
    driver.quit()