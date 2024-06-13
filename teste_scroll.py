import pyautogui
from time import sleep

pyautogui.moveTo(1189,522, duration=2)
for i in range(4):
    pyautogui.scroll(-1100)
    sleep(1)