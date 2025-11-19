from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import contribuinte_repository
from app.fastapi.schema.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate
from app.core.pagination import format_result
from app.core.exceptions import DuplicateEntryError, DatabaseError
from app.logger import app_logger


async def get_contribuintes_danfe_endereco(filtro_nome: str, page: int, db: AsyncSession):
    try:
        result = await contribuinte_repository.get_contribuintes_danfe_endereco(filtro_nome, page, db)
        return format_result(data=result, page=page)
    except Exception as e:
        app_logger.exception("Erro ao obter contribuintes, danfe e endereço %s", e)
        raise DatabaseError(str(e)) from e


async def get_contribuintes(page: int, db: AsyncSession):
    try:
        result = await contribuinte_repository.get_contribuintes(page=page, db=db)
        return format_result(data=result, page=page)
    except Exception as e:
        app_logger.exception("Erro ao obter contribuintes %s", e)
        raise DatabaseError(str(e)) from e


async def get_contribuinte_por_cd(cd_contribuinte: str, db: AsyncSession):
    try:
        result = await contribuinte_repository.get_contribuinte_por_cd(cd_contribuinte=cd_contribuinte, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao obter contribuinte por cd %s", e)
        raise DatabaseError(str(e)) from e


async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, db: AsyncSession):
    try:
        result = await contribuinte_repository.get_contribuinte_por_cnpj(cnpj_contribuinte=cnpj_contribuinte, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao obter contribuinte por cnpj %s", e)
        raise DatabaseError(str(e)) from e


async def create_contribuinte(contribuinte: ContribuinteCreate, db: AsyncSession):
    try:
        result = await contribuinte_repository.create_contribuinte(contribuinte=contribuinte, db=db)
        return format_result(data=result)
    except DuplicateEntryError as e:
        raise e
    except Exception as e:
        app_logger.exception("Erro ao criar contribuinte %s", e)
        raise DatabaseError(str(e)) from e


async def update_contribuinte(cd_contribuinte: str, contribuinte: ContribuinteUpdate, db: AsyncSession):
    try:
        result = await contribuinte_repository.update_contribuinte(cd_contribuinte=cd_contribuinte, contribuinte=contribuinte, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao atualizar contribuinte %s", e)
        raise DatabaseError(str(e)) from e


async def delete_contribuinte(cd_contribuinte: str, db: AsyncSession):
    try:
        result = await contribuinte_repository.delete_contribuinte(cd_contribuinte=cd_contribuinte, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao excluir contribuinte %s", e)
        raise DatabaseError(str(e)) from e
