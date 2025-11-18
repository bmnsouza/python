from sqlalchemy import text
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contribuinte_model import ContribuinteModel
from app.fastapi.schemas.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate
from app.utils.pagination import calculate_offset, format_result
from app.core.constants import DEFAULT_PAGE_SIZE


async def get_contribuintes_danfe_endereco(db: AsyncSession, filtro_nome: str, page: int = 1):
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

    result = await db.execute(query, params)
    data = [dict(row) for row in result.mappings().all()]
    return format_result(data=data, page=page)


async def get_contribuintes_paginado(db: AsyncSession, page: int = 1):
    query = (
        select(ContribuinteModel)
        .order_by(ContribuinteModel.nm_fantasia)
        .offset(calculate_offset(page))
        .limit(DEFAULT_PAGE_SIZE)
    )

    result = await db.execute(query)
    data = result.scalars().all()
    return format_result(data=data, page=page)


async def get_contribuintes(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(ContribuinteModel).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


async def get_contribuinte(db: AsyncSession, cd_contribuinte: str):
    query = (
        select(ContribuinteModel)
        .where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
    )
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
