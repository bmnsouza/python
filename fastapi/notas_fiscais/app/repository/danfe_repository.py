from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.exceptions import map_data_base_error
from app.core.pagination import DEFAULT_PAGE_SIZE, calculate_offset
from app.fastapi.schema.danfe_schema import DanfeCreate, DanfeFiltro, DanfeUpdate
from app.model.danfe_model import DanfeModel


async def get_danfes(page: int, session: AsyncSession):
    try:
        query = (
            select(DanfeModel)
            .order_by(DanfeModel.cd_contribuinte)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )
        result = await session.execute(statement=query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_danfes_filtradas(danfe: DanfeFiltro, page: int, session: AsyncSession):
    try:
        conditions = []

        if danfe.cd_contribuinte:
            conditions.append(DanfeModel.cd_contribuinte == danfe.cd_contribuinte)
        if danfe.numero:
            conditions.append(DanfeModel.numero == danfe.numero)
        if danfe.valor_minimo is not None:
            conditions.append(DanfeModel.valor_total >= danfe.valor_minimo)
        if danfe.valor_maximo is not None:
            conditions.append(DanfeModel.valor_total <= danfe.valor_maximo)
        if danfe.data_inicial:
            conditions.append(DanfeModel.data_emissao >= danfe.data_inicial)
        if danfe.data_final:
            conditions.append(DanfeModel.data_emissao <= danfe.data_final)

        query = select(DanfeModel)

        if conditions:
            query = query.where(and_(*conditions))

        query = (
            query.order_by(DanfeModel.id_danfe)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )

        result = await session.execute(statement=query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_danfe(id_danfe: int, session: AsyncSession):
    try:
        query = (
            select(DanfeModel)
            .where(DanfeModel.id_danfe == id_danfe)
        )
        result = await session.execute(statement=query)
        return result.scalars().first()
    except Exception as e:
        map_data_base_error(e)


async def create_danfe(danfe: DanfeCreate, session: AsyncSession):
    try:
        result = DanfeModel(**danfe.model_dump())
        session.add(result)
        await session.commit()
        await session.refresh(result)
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)


async def update_danfe(id_danfe: int, danfe: DanfeUpdate, session: AsyncSession):
    try:
        result = await get_danfe(id_danfe=id_danfe, session=session)
        if result:
            for key, value in danfe.model_dump(exclude_unset=True).items():
                setattr(result, key, value)
            await session.commit()
            await session.refresh(result)
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)


async def delete_danfe(id_danfe: int, session: AsyncSession):
    try:
        result = await get_danfe(id_danfe=id_danfe, session=session)
        if result:
            await session.delete(result)
            await session.commit()
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)
