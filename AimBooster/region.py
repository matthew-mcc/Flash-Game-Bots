import pyautogui
import time

time.sleep(2)
iml = pyautogui.screenshot(region=(574, 443, 751, 525))
iml.save(r"C:\GIT\Personal_Projects\Bots\AimBooster\savedimage.png")