import webbrowser
import pyautogui
from time import sleep

def definir_contatos():
    lista_contatos = []
    with open('telefones.txt','r') as arquivo:
        for linha in arquivo:
            lista_contatos.append(linha.split('\n')[0])

    if len(lista_contatos) == 0:
        lista_contatos = pyautogui.prompt(
            text='Digite os números de telefone separados por virgula. Ex: 41982342237, 44999675433',
            title='Campo obrigatório')
    return lista_contatos

def clicar_iniciar_conversa():
    pyautogui.leftClick(1356,324, duration=1)

def clicar_usar_whats_web():
    pyautogui.leftClick(1363,396, duration=1)

def clicar_digite_mensagem():
    pyautogui.leftClick(1463,1002, duration=1)

def mensagem_escolhida():
    texto = '''Oi Amor, estou com fome.'''
    pyautogui.typewrite(texto, interval=0.1)

def clicar_enviar():
    pyautogui.press('enter')

def bot_whatsapp(contatos):
    path = 'https://api.whatsapp.com/send?phone=55'
    for numero in contatos:
        webbrowser.open(f'{path}{numero}')
        sleep(3)
        clicar_iniciar_conversa()
        sleep(2)
        clicar_usar_whats_web()
        sleep(8)
        clicar_digite_mensagem()
        sleep(1)
        mensagem_escolhida()
        sleep(1)
        clicar_enviar() 

bot_whatsapp(contatos=definir_contatos())
