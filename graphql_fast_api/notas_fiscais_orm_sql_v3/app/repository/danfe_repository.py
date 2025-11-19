from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.danfe_model import DanfeModel
from app.core.exceptions import map_data_base_error
from app.fastapi.schema.danfe_schema import DanfeCreate, DanfeUpdate
from app.core.pagination import DEFAULT_PAGE_SIZE, calculate_offset


async def get_danfes(page: int, db: AsyncSession):
    try:
        query = (
            select(DanfeModel)
            .order_by(DanfeModel.cd_contribuinte)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )
        result = await db.execute(statement=query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_danfe(id_danfe: int, db: AsyncSession):
    try:
        query = (
            select(DanfeModel)
            .where(DanfeModel.id_danfe == id_danfe)
        )
        result = await db.execute(statement=query)
        return result.scalars().first()
    except Exception as e:
        map_data_base_error(e)


async def create_danfe(danfe: DanfeCreate, db: AsyncSession):
    try:
        result = DanfeModel(**danfe.model_dump())
        db.add(result)
        await db.commit()
        await db.refresh(result)
        return result
    except Exception as e:
        await db.rollback()
        map_data_base_error(e)


async def update_danfe(id_danfe: int, danfe: DanfeUpdate, db: AsyncSession):
    try:
        result = await get_danfe(id_danfe=id_danfe, db=db)
        if result:
            for key, value in danfe.model_dump(exclude_unset=True).items():
                setattr(result, key, value)
            await db.commit()
            await db.refresh(result)
        return result
    except Exception as e:
        await db.rollback()
        map_data_base_error(e)


async def delete_danfe(id_danfe: int, db: AsyncSession):
    try:
        result = await get_danfe(id_danfe=id_danfe, db=db)
        if result:
            await db.delete(result)
            await db.commit()
        return result
    except Exception as e:
        await db.rollback()
        map_data_base_error(e)
