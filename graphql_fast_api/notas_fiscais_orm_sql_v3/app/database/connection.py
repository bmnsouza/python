from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.middleware.sql_audit_middleware import setup_sql_audit
from app.database import config


class Base(DeclarativeBase):
    pass


DATABASE_URL = (
    f"oracle+oracledb_async://{config.ORACLE_USER}:{config.ORACLE_PASSWORD}"
    f"@{config.ORACLE_DSN}?service_name={config.ORACLE_SERVICE_NAME}"
)


engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)


setup_sql_audit(engine)
