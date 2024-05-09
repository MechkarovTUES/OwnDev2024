import pyautogui
import time

time.sleep(5)
for i in range(0,103):
    pyautogui.typewrite(str(i))
    pyautogui.press('enter')
    time.sleep(0.005)
