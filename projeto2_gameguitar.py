import pyautogui
import keyboard
from time import sleep

pyautogui.leftClick(1360,507, duration=1)
sleep(1)

verde = pyautogui.locateCenterOnScreen('verde.png')
sleep(1)
vermelho = pyautogui.locateCenterOnScreen('vermelho.png')
sleep(1)
amarelo = pyautogui.locateCenterOnScreen('amarelo.png')
sleep(1)
print(verde, vermelho, amarelo)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(verde[0],verde[1],(0,152,0)):
        print('A')
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(vermelho[0],vermelho[1],(255,0,0)):
        print('S')
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(amarelo[0],amarelo[1],(244,244,2)):
        print('J')
        pyautogui.press('j')
        sleep(0.05)