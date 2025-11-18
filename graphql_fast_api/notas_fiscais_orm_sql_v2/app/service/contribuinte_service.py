from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import contribuinte_repository
from app.core.pagination import format_result

async def get_contribuintes(page: int, db: AsyncSession):
    result = await contribuinte_repository.get_contribuintes(page, db)
    return format_result(data=result, page=page)


async def get_contribuinte_por_cd(cd_contribuinte: str, db: AsyncSession):
    result = await contribuinte_repository.get_contribuinte_por_cd(cd_contribuinte, db)
    return format_result(data=result)


async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, db: AsyncSession):
    result = await contribuinte_repository.get_contribuinte_por_cnpj(cnpj_contribuinte, db)
    return format_result(data=result)
