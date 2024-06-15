from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import random

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1100,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


def digitar_texto(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

driver = iniciar_driver()
# abrir o site
driver.get('https://www.facebook.com/')
sleep(4)

# encontrar elemento de email e digitar email
email = driver.find_element(By.ID, 'email')
sleep(5)
digitar_texto('email@gmail.com',email)
sleep(4)

# encontrar elemento de senha e digitar senha
senha = driver.find_element(By.ID, 'pass')
sleep(5)
digitar_texto('senha',senha)
sleep(4)

# encontrar elemento do botao entrar e clicar
entrar = driver.find_element(By.XPATH, '//button[@name="login"]')
sleep(2)
entrar.click()
sleep(8)

# encontrar elemento 'Em que estás a pensar, Adilson?' e clicar
campo_postagem = driver.find_element(By.XPATH, '//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
sleep(4)
campo_postagem.click()
sleep(4)

# encontrar elemento campo para escrever
campo_escrever = driver.find_element(By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
sleep(5)

# escrever uma mensagem humanizada
texto = 'Boa noite a todos, que Deus abençoe cada um de vocês.'
digitar_texto(texto, campo_escrever)
sleep(8)

# encontrar elemento botao 'Publicar' e clicar
botao_publicar = driver.find_element(By.XPATH, '//div[@aria-label="Publicar"]')
sleep(3)
botao_publicar.click()

input('')
driver.close()