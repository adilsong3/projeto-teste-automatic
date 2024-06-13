import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(2)
pyautogui.moveTo(1714,544, duration=1)
pyautogui.scroll(-712)
pyautogui.leftClick()
sleep(1)
pyautogui.typewrite('Adilson Gustavo')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(1543,188, duration=1)
sleep(1)
pyautogui.scroll(712)
sleep(2)
pyautogui.scroll(-2310)
pyautogui.click(972,194, duration=1)
pyautogui.click(1152,205, duration=1.5)
sleep(1)
pyautogui.alert(
    text='VOCÊ TERMINOU',
    title='Automação de SITE',
    button='ok'
)