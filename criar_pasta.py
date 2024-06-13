# 1º navegar até a pasta
# 2º clicar com botão direito do mouse
# 3º descer até novo, esperar
# 4º ir para a direita
# 5º clicar em pasta

import pyautogui
from time import sleep

pyautogui.moveTo(1369,490, duration=1)
pyautogui.rightClick(duration=2)
sleep(3)
pyautogui.move(20,285, duration=2)
sleep(2)
pyautogui.move(300,0, duration=2)
pyautogui.leftClick(duration=1)
pyautogui.moveTo(1088,348, duration=1)
pyautogui.leftClick(duration=1)