from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app import config
from app.middleware.sql_audit_middleware import setup_sql_audit

# ========================================
# BASE ORM (para todos os models herdarem)
# ========================================
class Base(DeclarativeBase):
    pass

# ========================================
# ENGINE ASYNC (Oracle)
# ========================================
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

# ========================================
# SESSION FACTORY
# ========================================
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ========================================
# DEPENDÊNCIA FASTAPI / GRAPHQL
# ========================================
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Retorna uma sessão assíncrona do SQLAlchemy (com tipagem correta)."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
