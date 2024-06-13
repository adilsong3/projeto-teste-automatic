import pyautogui
from time import sleep

for i in range(6):
    pyautogui.moveTo(1085,272, duration=1)
    pyautogui.dragTo(1228,923,duration=0.5, button='left')