from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2

img = cv2.imread(r"C:\GIT\Personal_Projects\Bots\AimBooster\x.png")

img_location = pyautogui.locateOnScreen(img, confidence=0.8)
while 1:
    if img_location != None:
        print("I can see it")
        print(img_location)
        time.sleep(0.5)
    else:
        print("Cannot see it")
        time.sleep(0.5)