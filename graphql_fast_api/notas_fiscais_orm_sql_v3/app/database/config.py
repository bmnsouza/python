import os
from dotenv import load_dotenv


# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# =====================================
# CONFIGURAÇÃO DO ORACLE
# =====================================
ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")
ORACLE_SERVICE_NAME = os.getenv("ORACLE_SERVICE_NAME")
