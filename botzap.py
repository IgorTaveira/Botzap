import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

midia = "poe o local da midia aqui"


contatos = []

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
driver.get('https://web.whatsapp.com')
time.sleep(25)

def ProcurarContato(contato):
        search_contato = driver.find_element(By.CLASS_NAME, value = 'iq0m558w')
        time.sleep(2)
        search_contato.click()
        search_contato.send_keys(contato)
        time.sleep(2)
        search_contato.send_keys(Keys.ENTER)

def enviar_midia(midia):
        search_image = driver.find_element(By.XPATH, value = "//span[@data-icon='clip']")
        search_image.click()
        attach = driver.find_element(By.XPATH, value = "//input[@type='file']")
        attach.send_keys(midia)
        time.sleep(3)
        botao_enviar = driver.find_element(By.CLASS_NAME, value = '_3wFFT')
        botao_enviar.click()
        time.sleep(2)

def enviar_mensagem(mensagem):

        chat_box = driver.find_element(By.CLASS_NAME, value = '_3Uu1_')
        chat_box.click()
        time.sleep(2)
        chat_box.send_keys('*POE A MENSAGEM AQUI *')
        botao_enviar2 = driver.find_element(By.XPATH, value = "//span[@data-icon='send']" )
        botao_enviar2.click()
          

for contato in contatos:
    ProcurarContato(contato)
    enviar_midia(midia)
    enviar_mensagem(mensagem)