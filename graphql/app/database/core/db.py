from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
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
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)

SessionFactory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_db_session():
    async with SessionFactory() as session:
        yield session


async def get_graphql_context():
    async with get_db_session() as session:
        yield {"session": session}


async def shutdown_db():
    await engine.dispose()
