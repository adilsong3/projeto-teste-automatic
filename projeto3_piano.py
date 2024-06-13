# site do jogo https://www.jogos360.com.br/piano_tiles_2_online.html#google_vignette

import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def inicio_game():
    # 1ª primeira tela, clicar para JOGAR >
    pyautogui.leftClick(1206,521, duration=1)
    sleep(10)

def pular_anuncio():
    # 2ª segunda tela, esperar o anuncio e clicar em pular
    pyautogui.leftClick(1583,610, duration=1)
    sleep(5)

def clicar_em_go():
    # 3ª terceira tela, clicar em GO
    pyautogui.leftClick(1232,515, duration=1)
    sleep(2)

def clicar_em_play():
    # 4ª quarta tela, clicar em PLAY
    pyautogui.leftClick(1232,515, duration=1)
    sleep(2)

def clicar_primeira_musica():
    # 5ª quinta tela, clicar na primeira musica
    pyautogui.leftClick(1237,309, duration=1)
    sleep(10)

def clicar_em_start():
    # 6ª sexta tela, clicar em START
    if pyautogui.pixelMatchesColor(1264,451, (54,159,198)):
        click(1124,443)
    if pyautogui.pixelMatchesColor(1195,451, (54,159,198)):
        click(1195,443)
    if pyautogui.pixelMatchesColor(1265,451, (54,159,198)):
        click(1265,443)
    if pyautogui.pixelMatchesColor(1333,451, (54,159,198)):
        click(1333,443)
    #start = pyautogui.locateCenterOnScreen('start.png')
    #sleep(1)
    #pyautogui.leftClick(start[0], start[1], duration=1)

def clicar_tecla_orientacao():
    # 7ª setima tela, clicar na tecla de orientação
    sleep(4)
    primeira_tecla = pyautogui.locateCenterOnScreen('primeiratecla.png')
    sleep(2)
    pyautogui.leftClick(primeira_tecla[0],primeira_tecla[1],duration=1)

def jogar():
    while keyboard.is_pressed('1') == False:
        if pyautogui.pixelMatchesColor(1124,443, (0,0,0)):
            click(1124,443)
            sleep(0.05)
        if pyautogui.pixelMatchesColor(1195,443, (0,0,0)):
            click(1195,443)
            sleep(0.05)
        if pyautogui.pixelMatchesColor(1265,443, (0,0,0)):
            click(1265,443)
            sleep(0.05)
        if pyautogui.pixelMatchesColor(1333,443, (0,0,0)):
            click(1333,443)
            sleep(0.05)
        #if pyautogui.pixelMatchesColor(1231,317, (246,174,0)):
        #    print('fim')
        #    break
        #elif pyautogui.pixelMatchesColor(1124,443, (225,111,116)):
        #    print('fim')
        #    break
        #elif pyautogui.pixelMatchesColor(1195,443, (225,111,116)):
        #    print('fim')
        #    break
        #elif pyautogui.pixelMatchesColor(1265,443, (225,111,116)):
        #    print('fim')
        #    break
        #elif pyautogui.pixelMatchesColor(1333,443, (225,111,116)):
        #    print('fim')
        #    break
        #elif pyautogui.locateCenterOnScreen('fimpianox.png') is not None:
        #    print('fim')
        #    break

def piano_tiles_2():
    inicio_game()
    pular_anuncio()
    clicar_em_go()
    clicar_em_play()
    clicar_primeira_musica()
    clicar_em_start()
    #clicar_tecla_orientacao()
    jogar()

piano_tiles_2()