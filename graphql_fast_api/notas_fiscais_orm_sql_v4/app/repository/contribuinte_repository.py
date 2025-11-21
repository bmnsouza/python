from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.exceptions import map_data_base_error
from app.core.pagination import DEFAULT_PAGE_SIZE, calculate_offset
from app.fastapi.schema.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate
from app.model.contribuinte_model import ContribuinteModel


async def get_contribuintes(page: int, session: AsyncSession):
    try:
        query = (
            select(ContribuinteModel)
            .order_by(ContribuinteModel.nm_fantasia)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )
        result = await session.execute(statement=query)
        return result.scalars().all()
    except Exception as e:
        map_data_base_error(e)


async def get_contribuintes_danfe_endereco(filtro_nome: str, page: int, session: AsyncSession):
    try:
        query = text("""
            SELECT c.CD_CONTRIBUINTE, c.CNPJ_CONTRIBUINTE, c.NM_FANTASIA,
                d.NUMERO, TO_CHAR(d.DATA_EMISSAO, 'dd/mm/yyyy') AS DATA_EMISSAO, d.VALOR_TOTAL,
                e.LOGRADOURO, e.MUNICIPIO, e.UF
            FROM NOTA_FISCAL.CONTRIBUINTE c JOIN NOTA_FISCAL.DANFE d ON d.CD_CONTRIBUINTE = c.CD_CONTRIBUINTE
            JOIN NOTA_FISCAL.ENDERECO e  ON e.CD_CONTRIBUINTE = c.CD_CONTRIBUINTE
            WHERE c.NM_FANTASIA LIKE :filtro_nome
            ORDER BY c.NM_FANTASIA, d.DATA_EMISSAO, d.VALOR_TOTAL
            OFFSET :page ROWS FETCH NEXT :page_size ROWS ONLY
        """)
        params = {
            "filtro_nome": f"%{filtro_nome}%",
            "page": calculate_offset(page),
            "page_size": DEFAULT_PAGE_SIZE   
        }
        result = await session.execute(statement=query, params=params)
        return [dict(row) for row in result.mappings().all()]
    except Exception as e:
        map_data_base_error(e)


async def get_contribuinte_por_cd(cd_contribuinte: str, session: AsyncSession):
    try:
        query = (
            select(ContribuinteModel)
            .where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
        )
        result = await session.execute(statement=query)
        return result.scalars().first()
    except Exception as e:
        map_data_base_error(e)


async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, session: AsyncSession):
    try:
        query = (
            select(ContribuinteModel)
            .where(ContribuinteModel.cnpj_contribuinte == cnpj_contribuinte)
        )
        result = await session.execute(statement=query)
        return result.scalars().first()
    except Exception as e:
        map_data_base_error(e)


async def create_contribuinte(contribuinte: ContribuinteCreate, session: AsyncSession):
    try:
        result = ContribuinteModel(**contribuinte.model_dump())
        session.add(result)
        await session.commit()
        await session.refresh(result)
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)


async def update_contribuinte(cd_contribuinte: str, contribuinte: ContribuinteUpdate, session: AsyncSession):
    try:
        result = await get_contribuinte_por_cd(cd_contribuinte=cd_contribuinte, session=session)
        if result:
            for key, value in contribuinte.model_dump(exclude_unset=True).items():
                setattr(result, key, value)
            await session.commit()
            await session.refresh(result)
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)


async def delete_contribuinte(cd_contribuinte: str, session: AsyncSession):
    try:
        result = await get_contribuinte_por_cd(cd_contribuinte=cd_contribuinte, session=session)
        if result:
            await session.delete(result)
            await session.commit()
        return result
    except Exception as e:
        await session.rollback()
        map_data_base_error(e)
