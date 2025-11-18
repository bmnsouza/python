from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.danfe_model import DanfeModel
from app.fastapi.schema.danfe_schema import DanfeCreate, DanfeUpdate


async def get_danfes(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(DanfeModel).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_danfe(db: AsyncSession, id_danfe: int):
    query = select(DanfeModel).where(DanfeModel.id_danfe == id_danfe)
    result = await db.execute(query)
    return result.scalars().first()

async def create_danfe(db: AsyncSession, danfe: DanfeCreate):
    db_danfe = DanfeModel(**danfe.model_dump())
    db.add(db_danfe)
    await db.commit()
    await db.refresh(db_danfe)
    return db_danfe

async def update_danfe(db: AsyncSession, id_danfe: int, updates: DanfeUpdate):
    db_danfe = await get_danfe(db, id_danfe)
    if not db_danfe:
        return None
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_danfe, key, value)
    await db.commit()
    await db.refresh(db_danfe)
    return db_danfe

async def delete_danfe(db: AsyncSession, id_danfe: int):
    db_danfe = await get_danfe(db, id_danfe)
    if db_danfe:
        await db.delete(db_danfe)
        await db.commit()
    return db_danfe
