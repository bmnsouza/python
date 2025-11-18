from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from .connection import engine


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Retorna uma sessão assíncrona do SQLAlchemy (com tipagem correta)."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
