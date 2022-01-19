from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2

time.sleep(2)
#color = RGB: (255, 219, 195)
#region = (574, 443, 751, 525)
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(575, 445, 750, 525))
    width, height = pic.size


    for i in range(0, width, 5):
        for k in range(0, height, 5):
            r,g,b = pic.getpixel((i,k))

            if b == 195:
                click(i+575, k+445)
                time.sleep(0.15)
                break