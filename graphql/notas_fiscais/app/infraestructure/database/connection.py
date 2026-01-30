from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core import config


class Base(DeclarativeBase):
    pass


DATABASE_URL = (
    f"oracle+oracledb_async://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}:{config.DB_PORT}/"
    f"?service_name={config.DB_SERVICE}"
)


engine = create_async_engine(
    DATABASE_URL,
    echo=False,

    # Pool de conexões
    pool_size=10, # Conexões abertas simultaneamente
    max_overflow=20, # Conexões extras em pico
    pool_timeout=30, # Tempo máximo de espera por conexão
    pool_recycle=1800, # Recicla conexões antigas (segundos)
    pool_pre_ping=True, # Testa conexão antes de usar
)
