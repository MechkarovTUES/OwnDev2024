import pyautogui
import time
while True:
    print(pyautogui.position())
    x, y = pyautogui.position()
    print((x-8.5)*2, (y-8.5)*2)
    time.sleep(0.1)