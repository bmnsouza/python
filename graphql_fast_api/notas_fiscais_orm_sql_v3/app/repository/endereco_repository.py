from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.endereco_model import EnderecoModel
from app.fastapi.schema.endereco_schema import EnderecoCreate, EnderecoUpdate
from app.core.exceptions import map_data_base_error
from app.core.pagination import DEFAULT_PAGE_SIZE, calculate_offset


async def get_enderecos(page: int, db: AsyncSession):
    try:
        query = (
            select(EnderecoModel)
            .order_by(EnderecoModel.logradouro)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )
        result = await db.execute(statement=query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_endereco(id_endereco: int, db: AsyncSession):
    try:
        query = (
            select(EnderecoModel)
            .where(EnderecoModel.id_endereco == id_endereco)
        )
        result = await db.execute(query)
        return result.scalars().first()
    except Exception as e:
        map_data_base_error(e)


async def create_endereco(endereco: EnderecoCreate, db: AsyncSession):
    try:
        result = EnderecoModel(**endereco.model_dump())
        db.add(result)
        await db.commit()
        await db.refresh(result)
        return result
    except Exception as e:
        await db.rollback()
        map_data_base_error(e)


async def update_endereco(id_endereco: int, endereco: EnderecoUpdate, db: AsyncSession):
    try:
        result = await get_endereco(id_endereco=id_endereco, db=db)
        if result:
            for key, value in endereco.model_dump(exclude_unset=True).items():
                setattr(result, key, value)
            await db.commit()
            await db.refresh(result)
        return result
    except Exception as e:
        await db.rollback()
        map_data_base_error(e)


async def delete_endereco(id_endereco: int, db: AsyncSession):
    try:
        result = await get_endereco(id_endereco=id_endereco, db=db)
        if result:
            await db.delete(result)
            await db.commit()
        return result
    except Exception as e:
        await db.rollback()
        map_data_base_error(e)
