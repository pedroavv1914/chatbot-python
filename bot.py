from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import logging
from conversation_manager import ConversationManager

# Configuração de logging para o bot.py
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configurações do banco de dados (ajuste conforme seu ambiente)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bot_curso'
}

# Inicializa o gerenciador de conversa
conversation_manager = ConversationManager(db_config)

# Definindo seletores diretamente no código (removendo dependência da API externa)
# ATENÇÃO: Estes seletores podem mudar com atualizações do WhatsApp Web.
# Você precisará monitorar e ajustar se o bot parar de funcionar.
bolinha_notificacao = '_ao3e' # Exemplo, ajuste conforme necessário
contato_cliente = '//*[@id="main"]/header/div[2]/div[1]/div/span' # Exemplo, ajuste conforme necessário
caixa_msg = '_akbu' # Exemplo, ajuste conforme necessário
msg_cliente = '_akbu' # Exemplo, ajuste conforme necessário
caixa_msg2 = '_akbu' # Exemplo, ajuste conforme necessário
caixa_pesquisa = 'input[title="Pesquisar ou começar uma nova conversa"]' # Exemplo, ajuste conforme necessário

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

usuario = 'botbala@gmail.com'
dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(options = chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
    try:
        
        #CAPTURAR A BOLINHA
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(1)

        #PEGAR O TELEFONE
        telefone_cliente = driver.find_element(By.XPATH,contato_cliente)
        telefone_final = telefone_cliente.text 
        print(telefone_final)
        time.sleep(1)

        #PEGAR A MSG DO CLIENTE
        todas_as_msg = driver.find_elements(By.CLASS_NAME, '_akbu')
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)
        time.sleep(1)

        #RESPONDENDO CLIENTE
        resposta = conversation_manager.get_bot_response(telefone_final, msg, usuario)
        campo_de_texto = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
        campo_de_texto.click()
        time.sleep(1)
        campo_de_texto.send_keys(resposta, Keys.ENTER)

        #FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    except Exception as e:
        logging.error(f'Ocorreu um erro no bot: {e}')
        logging.info('AGUARDANDO NOVAS MENSAGENS')
        # Em caso de erro, pode ser útil tentar fechar o contato para evitar loops
        try:
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        except Exception as esc_e:
            logging.warning(f'Erro ao tentar fechar contato após falha: {esc_e}')

while True:
    bot()