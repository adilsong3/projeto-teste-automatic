import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.moveTo(1306,547, duration=2)
pyautogui.click(duration=1)
escrever_frase('Olá, teste escrita ')
