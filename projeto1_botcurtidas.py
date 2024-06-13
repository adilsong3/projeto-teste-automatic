import webbrowser
import pyautogui
from time import sleep

# solicitando email e senha para o usuário
login = pyautogui.prompt(text='Digite seu e-mail ou usuário', title='obrigatório')
senha = pyautogui.password(text='Digite sua senha', title='obrigatório', mask='*')

# Função para deslogar
def logout():
    fechar = pyautogui.locateCenterOnScreen('fechar.png')
    pyautogui.click(fechar[0],fechar[1], duration=1)
    sleep(1)
    menu = pyautogui.locateCenterOnScreen('menu.png')
    pyautogui.click(menu[0],menu[1], duration=1)
    sleep(1)
    pyautogui.move(100,0)
    sleep(1)
    pyautogui.leftClick(duration=1)
    sleep(1)

while True:
    if login is None or senha is None:
        pyautogui.alert(text='Preencha seu Login e Senha', title='Automação interrompida')
        break 
    # 1º entrar no site
    webbrowser.open('https://www.instagram.com/')
    # 2º clicar e digitar login
    sleep(1)
    #pyautogui.click(1533,360, duration=2)
    email = pyautogui.locateCenterOnScreen('email.png')
    pyautogui.click(email[0],email[1], duration=2)
    sleep(2)
    pyautogui.typewrite(login, interval=0.2)
    sleep(1)
    # 3º apertar tab e digitar senha
    pyautogui.press('tab')
    sleep(3)
    pyautogui.typewrite(senha, interval=0.2)
    # 4º apertar tab 2x e apertar enter
    sleep(1)
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('enter')
    sleep(5)
    # 5º localizar e clicar em agora não
    agora_nao = pyautogui.locateCenterOnScreen('agoranao.png')
    pyautogui.click(agora_nao[0],agora_nao[1], duration=1)
    sleep(2)
    # 6º localizar e clicar em pesquisar (cordenada pesquisar 860,271)
    pesquisar = pyautogui.locateCenterOnScreen('pesquisar.png')
    pyautogui.click(pesquisar[0],pesquisar[1], duration=1)
    sleep(2)
    # 7º digitar a pagina que deseja
    pyautogui.typewrite('alcancecuritiba',interval=0.2)
    sleep(2)
    # 8º localizar a pagina Apertando tab 2x e depois enter
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('enter')
    sleep(5)
    # 9º localizar PUBLICAÇÕES andar 30 pixels X esquerda e 50 y baixo
    publi = pyautogui.locateCenterOnScreen('publi.png')
    pyautogui.moveTo(publi[0],publi[1], duration=1)
    sleep(1)
    pyautogui.move(-80, 80, duration=1)
    # 10º Clicar na publicação esperar 2 segundos
    sleep(1)
    pyautogui.leftClick()
    # 11º Localizar coração de curtir e verificar
    sleep(6)
    coracao = pyautogui.locateCenterOnScreen('jacurti.png')
    sleep(1)
    if coracao is not None:
        logout()
        pyautogui.alert(text='Publicação Já Curtida Anteriormente', title='Automação de instagran')
    elif coracao == None:
        naocurti = pyautogui.locateCenterOnScreen('jacurti.png')
        pyautogui.click(naocurti[0],naocurti[1], duration=1)
        sleep(1)
        logout()
        pyautogui.alert(text='Publicação Curtida com Sucesso', title='Automação de instagran')

