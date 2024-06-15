# versão valida para o dia 14/06/2024

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada

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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait

def digitar_texto(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

driver, wait = iniciar_driver()
# driver.implicitly_wait(10)

# abrir o site
driver.get('https://www.instagram.com/')
sleep(5)

#driver.execute_script("window.scrollTo(0, 300);")
#sleep(3)

# digitar email
email = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
sleep(2)
email.send_keys('vivimarcondes22')
sleep(2)

# digitar senha
senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
sleep(2)
senha.send_keys('Viviane@@1')
sleep(2)

# clicar entrar
entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
entrar.click()
sleep(8)

# paginas
paginas = ['devaprender']

# abrir nova aba
for pagina in paginas:
    driver.get(f'https://www.instagram.com/{pagina}')
    sleep(6)
    postagens = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="_aagu"]')))
    sleep(2)
    postagens[0].click()
    sleep(5)
    try:
        curtida = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//div[@role="button"]//div//span//*[@aria-label="Descurtir"]')))
        sleep(4)
        '''/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]//*[@aria-label="Curtir"]'''
    except:
        print(f'{pagina} - Postagem já curtida.')
    else:
        curtir = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//div[@role="button"]//div//span[@class="x1ykxiw6 x1ahuga x4hg4is x3oybdh"]')))
        '''/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]//div[@role="button"]'''
        sleep(3)
        driver.execute_script('arguments[0].click()', curtir)
        print(f'{pagina} - Postagem curtida com sucesso.')
    # //div[@role="button"]//div//span[@class="x1ykxiw6 x1ahuga x4hg4is x3oybdh"]//*[@aria-label="Descurtir"]
    sleep(4)

input('')
driver.close()