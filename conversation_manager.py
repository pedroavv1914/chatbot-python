import mysql.connector
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConversationManager:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None
        self.cursor = None
        self._connect()

    def _connect(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            logging.info("Conexão com o banco de dados estabelecida com sucesso.")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao conectar ao banco de dados: {err}")
            # Em um ambiente de produção, você pode querer levantar uma exceção ou ter uma estratégia de reconexão

    def _close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
            logging.info("Conexão com o banco de dados fechada.")

    def get_bot_response(self, phone_number, incoming_message, user_id):
        if not self.conn or not self.conn.is_connected():
            logging.warning("Tentando reconectar ao banco de dados...")
            self._connect()
            if not self.conn or not self.conn.is_connected():
                return "Desculpe, não consegui me conectar ao banco de dados. Tente novamente mais tarde."

        try:
            # 1. Buscar usuário pelo telefone
            sql = "SELECT status FROM usuario WHERE telefone = %s"
            self.cursor.execute(sql, (phone_number,))
            result = self.cursor.fetchone()

            user_status = 0 # Default status if user not found
            if result:
                user_status = result[0]
                logging.info(f"Usuário {phone_number} encontrado com status: {user_status}")
            else:
                # 2. Inserir novo usuário se não existir
                sql = "INSERT INTO usuario (telefone, status) VALUES (%s, %s)"
                self.cursor.execute(sql, (phone_number, 1))
                self.conn.commit()
                user_status = 1
                logging.info(f"Novo usuário {phone_number} inserido com status inicial: {user_status}")
                return self._get_menu_message(0) # Mensagem de boas-vindas para novo usuário

            # 3. Lógica de resposta baseada no status e mensagem
            response_message = ""
            next_status = user_status + 1

            # Simula a lógica do index.php
            if user_status == 1:
                response_message = self._get_menu_message(1)
            elif user_status == 2:
                response_message = self._get_menu_message(2)
            elif user_status == 3:
                response_message = self._get_menu_message(3)
            elif user_status == 4:
                response_message = self._get_menu_message(4)
            elif user_status >= 5:
                response_message = self._get_menu_message(5)
                next_status = 1 # Reinicia o fluxo

            # 4. Atualizar status do usuário
            sql = "UPDATE usuario SET status = %s WHERE telefone = %s"
            self.cursor.execute(sql, (next_status, phone_number))
            self.conn.commit()
            logging.info(f"Status do usuário {phone_number} atualizado para: {next_status}")

            return response_message

        except mysql.connector.Error as err:
            logging.error(f"Erro no banco de dados ao processar requisição: {err}")
            self.conn.rollback() # Reverte a transação em caso de erro
            return "Desculpe, ocorreu um erro interno ao processar sua solicitação."
        except Exception as e:
            logging.error(f"Erro inesperado ao processar requisição: {e}")
            return "Desculpe, ocorreu um erro inesperado. Por favor, tente novamente."

    def _get_menu_message(self, status_code):
        # Mapeia os status para as mensagens correspondentes
        menus = {
            0: "Bem-vindo à Pizzarium! Que bom ter você aqui! Sou o Cheffino e estou aqui para ajudá-lo a fazer seu pedido de forma rápida e fácil. \nPara começar, digite CARDÁPIO para ver nossas opções de pizzas. \nHorário de atendimento: de Terça - Domingo, 16:00 as 00:00. Endereço: Rua Palestra Itália 51.\nEstamos prontos para preparar sua pizza favorita!",
            1: "Bem-vindo à Pizzarium! Que bom ter você aqui! Sou o Cheffino e estou aqui para ajudá-lo a fazer seu pedido de forma rápida e fácil. \nPara começar, digite CARDÁPIO para ver nossas opções de pizzas. \nHorário de atendimento: de Terça - Domingo, 16:00 as 00:00. Endereço: Rua Palestra Itália 51.\nEstamos prontos para preparar sua pizza favorita!",
            2: "CARDÁPIO DA Pizzarium\nDescubra nossas delícias, feitas com amor e ingredientes fresquinhos!\n\n...:PIZZAS CONVENCIONAIS:...\nMUSSARELA = Molho de tomate, queijo mussarela e orégano. Tamanho: Média R$30 | Grande R$40\n\nCALABRESA = Molho de tomate, calabresa fatiada, cebola e orégano. Tamanho: Média R$32 | Grande R$42\n\nMARGUERITA= Molho de tomate, mussarela, tomate fresco e manjericão. Tamanho: Média R$33 | Grande R$43\n\nFRANGO COM CATUPIRY = Frango desfiado, molho de tomate, catupiry e orégano. Tamanho: Média R$35 | Grande R$45\n\nPORTUGUESA = Molho de tomate, mussarela, presunto, ovo, cebola, azeitonas e orégano. Tamanho: Média R$35 | Grande R$45\n\nNAPOLITANA = Molho de tomate, mussarela, parmesão, tomate fresco e orégano.Tamanho: Média R$34 | Grande R$44\n\nQUATRO QUEIJOS = Mussarela, gorgonzola, parmesão e catupiry. Tamanho: Média R$36 | Grande R$46\n\n...:PIZZAS ESPECIAIS:...\n\nPICANHA BBQ = Picanha desfiada, molho barbecue, mussarela e cebola caramelizada. Tamanho: Média R$45 | Grande R$55\n\nITÁLIA PREMIUM = Molho de tomate, mussarela de búfala, presunto de parma e rúcula. Tamanho: Média R$50 | Grande R$60\n\nDOCE DELÍCIA = Base de chocolate ao leite, morangos frescos e granulado crocante. Tamanho: Média R$38 | Grande R$48",
            3: "Você prefere pegar aqui, ou que seja entregue?",
            4: "Qual método de pagamento você prefere? (PIX, Cartão Crédito/Débito, Dinheiro.)",
            5: "Pedido confirmado! O prazo de entrega é de 20 - 40 minutos.\nMuito obrigado pela preferência!"
        }
        return menus.get(status_code, "Desculpe, não entendi. Poderia repetir?")

# Exemplo de uso (para testes, não será executado diretamente pelo bot.py)
if __name__ == "__main__":
    # Configurações do banco de dados (substitua pelos seus dados reais)
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'bot_curso'
    }

    manager = ConversationManager(db_config)

    # Simula uma nova mensagem de um cliente
    print("\n--- Nova Conversa ---")
    response = manager.get_bot_response("5511999999999", "Olá", "botbala@gmail.com")
    print(f"Bot responde: {response}")

    # Simula a próxima mensagem do mesmo cliente
    print("\n--- Próxima Mensagem ---")
    response = manager.get_bot_response("5511999999999", "CARDÁPIO", "botbala@gmail.com")
    print(f"Bot responde: {response}")

    # Simula outro cliente
    print("\n--- Outra Conversa ---")
    response = manager.get_bot_response("5521888888888", "Oi", "botbala@gmail.com")
    print(f"Bot responde: {response}")

    manager._close()
