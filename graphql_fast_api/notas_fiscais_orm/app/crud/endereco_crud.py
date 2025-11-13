from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.endereco_model import EnderecoModel
from app.fastapi.schemas.endereco_schema import EnderecoCreate, EnderecoUpdate


async def get_enderecos(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(EnderecoModel).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_endereco(db: AsyncSession, id_endereco: int):
    query = select(EnderecoModel).where(EnderecoModel.id_endereco == id_endereco)
    result = await db.execute(query)
    return result.scalars().first()

async def create_endereco(db: AsyncSession, endereco: EnderecoCreate):
    db_endereco = EnderecoModel(**endereco.model_dump())
    db.add(db_endereco)
    await db.commit()
    await db.refresh(db_endereco)
    return db_endereco

async def update_endereco(db: AsyncSession, id_endereco: int, updates: EnderecoUpdate):
    db_endereco = await get_endereco(db, id_endereco)
    if not db_endereco:
        return None
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_endereco, key, value)
    await db.commit()
    await db.refresh(db_endereco)
    return db_endereco

async def delete_endereco(db: AsyncSession, id_endereco: int):
    db_endereco = await get_endereco(db, id_endereco)
    if db_endereco:
        await db.delete(db_endereco)
        await db.commit()
    return db_endereco
