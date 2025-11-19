from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import danfe_repository
from app.fastapi.schema.danfe_schema import DanfeCreate, DanfeUpdate
from app.core.pagination import format_result
from app.core.exceptions import DuplicateEntryError, DatabaseError
from app.logger import app_logger


async def get_danfes(page: int, db: AsyncSession):
    try:
        result = await danfe_repository.get_danfes(page=page, db=db)
        return format_result(data=result, page=page)
    except Exception as e:
        app_logger.exception("Erro ao obter danfes %s", e)
        raise DatabaseError(str(e)) from e


async def get_danfe(id_danfe: str, db: AsyncSession):
    try:
        result = await danfe_repository.get_danfe(id_danfe=id_danfe, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao obter danfe %s", e)
        raise DatabaseError(str(e)) from e


async def create_danfe(danfe: DanfeCreate, db: AsyncSession):
    try:
        result = await danfe_repository.create_danfe(danfe=danfe, db=db)
        return format_result(data=result)
    except DuplicateEntryError as e:
        raise e
    except Exception as e:
        app_logger.exception("Erro ao criar danfe %s", e)
        raise DatabaseError(str(e)) from e


async def update_danfe(id_danfe: str, danfe: DanfeUpdate, db: AsyncSession):
    try:
        result = await danfe_repository.update_danfe(id_danfe=id_danfe, danfe=danfe, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao atualizar danfe %s", e)
        raise DatabaseError(str(e)) from e


async def delete_danfe(id_danfe: str, db: AsyncSession):
    try:
        result = await danfe_repository.delete_danfe(id_danfe=id_danfe, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao excluir danfe %s", e)
        raise DatabaseError(str(e)) from e
