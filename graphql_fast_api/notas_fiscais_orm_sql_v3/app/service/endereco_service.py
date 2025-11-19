from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import endereco_repository
from app.fastapi.schema.endereco_schema import EnderecoCreate, EnderecoUpdate
from app.core.pagination import format_result
from app.core.exceptions import DuplicateEntryError, DatabaseError
from app.logger import app_logger


async def get_enderecos(page: int, db: AsyncSession):
    try:
        result = await endereco_repository.get_enderecos(page=page, db=db)
        return format_result(data=result, page=page)
    except Exception as e:
        app_logger.exception("Erro ao obter endereços %s", e)
        raise DatabaseError(str(e)) from e


async def get_endereco(id_endereco: str, db: AsyncSession):
    try:
        result = await endereco_repository.get_endereco(id_endereco=id_endereco, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao obter endereço %s", e)
        raise DatabaseError(str(e)) from e


async def create_endereco(endereco: EnderecoCreate, db: AsyncSession):
    try:
        result = await endereco_repository.create_endereco(endereco=endereco, db=db)
        return format_result(data=result)
    except DuplicateEntryError as e:
        raise e
    except Exception as e:
        app_logger.exception("Erro ao criar endereço %s", e)
        raise DatabaseError(str(e)) from e


async def update_endereco(id_endereco: str, endereco: EnderecoUpdate, db: AsyncSession):
    try:
        result = await endereco_repository.update_endereco(id_endereco=id_endereco, endereco=endereco, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao atualizar endereço %s", e)
        raise DatabaseError(str(e)) from e


async def delete_endereco(id_endereco: str, db: AsyncSession):
    try:
        result = await endereco_repository.delete_endereco(id_endereco=id_endereco, db=db)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao excluir endereço %s", e)
        raise DatabaseError(str(e)) from e
