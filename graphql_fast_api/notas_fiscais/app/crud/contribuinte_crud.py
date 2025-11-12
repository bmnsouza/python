from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contribuinte_model import ContribuinteModel
from app.fastapi.schemas.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate


async def get_contribuintes(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(ContribuinteModel).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_contribuinte(db: AsyncSession, cd_contribuinte: str):
    query = select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
    result = await db.execute(query)
    return result.scalars().first()

async def create_contribuinte(db: AsyncSession, contribuinte: ContribuinteCreate):
    db_contribuinte = ContribuinteModel(**contribuinte.model_dump())
    db.add(db_contribuinte)
    await db.commit()
    await db.refresh(db_contribuinte)
    return db_contribuinte

async def update_contribuinte(db: AsyncSession, cd_contribuinte: str, updates: ContribuinteUpdate):
    db_contribuinte = await get_contribuinte(db, cd_contribuinte)
    if not db_contribuinte:
        return None
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_contribuinte, key, value)
    await db.commit()
    await db.refresh(db_contribuinte)
    return db_contribuinte

async def delete_contribuinte(db: AsyncSession, cd_contribuinte: str):
    db_contribuinte = await get_contribuinte(db, cd_contribuinte)
    if db_contribuinte:
        await db.delete(db_contribuinte)
        await db.commit()
    return db_contribuinte
