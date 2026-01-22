from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.database import config
from app.middleware.sql_audit_middleware import setup_sql_audit


class Base(DeclarativeBase):
    pass


DATABASE_URL = (
    f"oracle+oracledb_async://{config.ORACLE_USER}:{config.ORACLE_PASSWORD}"
    f"@{config.ORACLE_DSN}?service_name={config.ORACLE_SERVICE_NAME}"
)



engine = create_async_engine(
    DATABASE_URL,
    echo=False,

    # Pool
    pool_size=10, # Conexões abertas simultaneamente
    max_overflow=20, # Conexões extras em pico
    pool_timeout=30, # Tempo máximo de espera por conexão
    pool_recycle=1800, # Recicla conexões antigas (segundos)
    pool_pre_ping=True, # Testa conexão antes de usar
)


setup_sql_audit(engine)
