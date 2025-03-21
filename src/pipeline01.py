import time
import requests
import os
import logging
import logfire
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging import basicConfig, getLogger

logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = logging.getLogger(__name__)  # __name__ é o nome do arquivo atual  
logger.setLevel(logging.INFO) # Define o nível de log para INFO
logfire.instrument_requests()  # Injeta o log do requests
logfire.instrument_sqlalchemy()  # Injeta o log do SQLAlchemy
#---------------------------------------------

# Import Base and BitcoinPrice from database.py
from database import Base, BitcoinPrice

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis sepadas do arquivo .env (Sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão do SQLAlchemy
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_table():
    # Cria a tabela no banco de dados, se ela não existir
    Base.metadata.create_all(engine)
    print("Table created/Verify success!")


def extract_data():
    url = "https://api.coinbase.com/v2/prices/spot"
    params = {"currency": "USD"}
    response = requests.get(url, params=params)
    return response.json()['data']

def transform_data_bitcoin(response):
    value = response['amount']
    crypto = response['base']
    currency = response['currency']

    data_transformed = {
        'crypto': crypto,
        'currency': currency,
        'value': value
    }
    return data_transformed

def save_data_postgres(data):
    # Save data to PostgreSQL
    session = Session()
    new_data = BitcoinPrice(**data)
    session.add(new_data)
    session.commit()
    session.close()
    print("Data saved to PostgreSQL")

if __name__ == "__main__":
    create_table()
    logger.info("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extract_data()
            if dados_json:
                # data
                data_transformed = transform_data_bitcoin(dados_json)
                logger.info(f"Dados Tratados: {data_transformed}")
                save_data_postgres(data_transformed)
            time.sleep(15)
        except KeyboardInterrupt:
            logger.info("Processo interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            logger.error(f"Erro durante a execução: {e}")
            time.sleep(15)


