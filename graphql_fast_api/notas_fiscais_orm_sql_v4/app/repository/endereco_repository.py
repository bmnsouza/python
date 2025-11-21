from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.endereco_model import EnderecoModel
from app.fastapi.schema.endereco_schema import EnderecoCreate, EnderecoUpdate
from app.core.exceptions import map_data_base_error
from app.core.pagination import DEFAULT_PAGE_SIZE, calculate_offset


async def get_enderecos(page: int, session: AsyncSession):
    try:
        query = (
            select(EnderecoModel)
            .order_by(EnderecoModel.logradouro)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )
        result = await session.execute(statement=query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_enderecos_por_contribuinte(cd_contribuinte: str, page: int, session: AsyncSession):
    try:
        query = (
            select(EnderecoModel)
            .where(EnderecoModel.cd_contribuinte == cd_contribuinte)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_endereco(id_endereco: int, session: AsyncSession):
    try:
        query = (
            select(EnderecoModel)
            .where(EnderecoModel.id_endereco == id_endereco)
        )
        result = await session.execute(query)
        return result.scalars().first()
    except Exception as e:
        map_data_base_error(e)


async def create_endereco(endereco: EnderecoCreate, session: AsyncSession):
    try:
        result = EnderecoModel(**endereco.model_dump())
        session.add(result)
        await session.commit()
        await session.refresh(result)
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)


async def update_endereco(id_endereco: int, endereco: EnderecoUpdate, session: AsyncSession):
    try:
        result = await get_endereco(id_endereco=id_endereco, session=session)
        if result:
            for key, value in endereco.model_dump(exclude_unset=True).items():
                setattr(result, key, value)
            await session.commit()
            await session.refresh(result)
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)


async def delete_endereco(id_endereco: int, session: AsyncSession):
    try:
        result = await get_endereco(id_endereco=id_endereco, session=session)
        if result:
            await session.delete(result)
            await session.commit()
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)
