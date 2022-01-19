from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#first row = x: 510, y: 813
#second row = x: 616, y :813
#third row = x: 729, y: 813
#fourth row = x: 840, y: 813


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(510, 400)[0] == 0:
        click(510, 400)

    if pyautogui.pixel(616, 400)[0] == 0:
        click(616, 400)

    if pyautogui.pixel(729, 400)[0] == 0:
        click(729, 400)

    if pyautogui.pixel(840, 400)[0] == 0:
        click(840, 400)