from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DatabaseError, DuplicateEntryError
from app.core.logger import app_logger
from app.core.pagination import format_result
from app.fastapi.schema.endereco_schema import EnderecoCreate, EnderecoUpdate
from app.repository import endereco_repository


async def get_enderecos(page: int, session: AsyncSession):
    try:
        result = await endereco_repository.get_enderecos(page=page, session=session)
        return format_result(data=result, page=page)
    except Exception as e:
        app_logger.exception("Erro ao obter endereços %s", e)
        raise DatabaseError(str(e)) from e


async def get_enderecos_por_contribuinte(cd_contribuinte: str, page: int, session: AsyncSession):
    try:
        result = await endereco_repository.get_enderecos_por_contribuinte(cd_contribuinte=cd_contribuinte, page=page, session=session)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao obter endereços %s", e)
        raise DatabaseError(str(e)) from e


async def get_endereco(id_endereco: int, session: AsyncSession):
    try:
        result = await endereco_repository.get_endereco(id_endereco=id_endereco, session=session)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao obter endereço %s", e)
        raise DatabaseError(str(e)) from e


async def create_endereco(endereco: EnderecoCreate, session: AsyncSession):
    try:
        result = await endereco_repository.create_endereco(endereco=endereco, session=session)
        return format_result(data=result)
    except DuplicateEntryError as e:
        raise e
    except Exception as e:
        app_logger.exception("Erro ao criar endereço %s", e)
        raise DatabaseError(str(e)) from e


async def update_endereco(id_endereco: str, endereco: EnderecoUpdate, session: AsyncSession):
    try:
        result = await endereco_repository.update_endereco(id_endereco=id_endereco, endereco=endereco, session=session)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao atualizar endereço %s", e)
        raise DatabaseError(str(e)) from e


async def delete_endereco(id_endereco: str, session: AsyncSession):
    try:
        result = await endereco_repository.delete_endereco(id_endereco=id_endereco, session=session)
        return format_result(data=result)
    except Exception as e:
        app_logger.exception("Erro ao excluir endereço %s", e)
        raise DatabaseError(str(e)) from e
