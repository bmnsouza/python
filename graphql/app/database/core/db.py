from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core import config

settings = config.get_settings()


class Base(DeclarativeBase):
    pass


DATABASE_URL = (
    f"oracle+oracledb_async://{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/"
    f"?service_name={settings.db_service}"
)


engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_size=50,
    max_overflow=50,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)


session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_db_session():
    async with session_factory() as session:
        yield session


async def get_graphql_context():
    async with get_db_session() as session:
        yield {"session": session}


async def shutdown_db():
    await engine.dispose()
