from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2


time.sleep(2)
img = cv2.imread(r"C:\GIT\Personal_Projects\Bots\Exit_Clicker\exit.png")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    img_location = pyautogui.locateOnScreen(img, confidence=0.8)
    
    if img_location != None:
        x_coord = img_location[0]
        y_coord = img_location[1]
        click(x_coord, y_coord)
        time.sleep(0.05)

