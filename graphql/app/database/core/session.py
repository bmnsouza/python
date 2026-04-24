from typing import AsyncGenerator

from sqlalchemy import engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Retorna uma sessão assíncrona do SQLAlchemy"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
