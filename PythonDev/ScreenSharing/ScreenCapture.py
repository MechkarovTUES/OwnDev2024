import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui


def getPos():
    x, y = pyautogui.position()
    return int((x-8.5)*2), int((y-8.5)*2)


bounding_box = {'top':0, 'left':0, 'width': 1000, 'height': 650}


with mss() as sct:
    while True:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        # Paste the resized cursor image onto the screenshot
        img.paste(Image.open("default.png"), getPos(), Image.open("default.png"))

        # Convert the PIL image to a format suitable for OpenCV
        screen = np.array(img) 
        screen = screen[:, :, ::-1].copy() 

        # Display the image with the cursor in a window
        cv2.imshow('Display', cv2.resize(screen, (1440, 900) , interpolation=cv2.INTER_LINEAR))

        # Exit the loop if 'q' is pressed
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            print("Exiting...")
            cv2.destroyAllWindows()
            break