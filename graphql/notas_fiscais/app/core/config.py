import os

from dotenv import load_dotenv


# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do Oracle
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "1521"))
DB_SERVICE = os.getenv("DB_SERVICE")


# Validação mínima
if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_SERVICE]):
    raise RuntimeError("Variáveis de ambiente do banco não configuradas corretamente")
