from typing import Any, Dict, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logger import app_logger
from app.fastapi.schema.endereco_schema import Endereco, EnderecoListItem
from app.repository.endereco_repository import EnderecoRepository
from app.core.exception.exception_core import map_data_base_error


class EnderecoService:
    def __init__(self, session: AsyncSession):
        self.repo = EnderecoRepository(session=session)


    async def get_list(self, filters: dict, order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count(filters=filters)
            rows = await self.repo.get_list(offset=offset, limit=limit, filters=filters, order=order)

            return total, [Endereco.model_validate(r) for r in rows]
        except Exception as e:
            app_logger.exception("Erro ao obter endereços %s", e)
            map_data_base_error(e)


    async def get_list_sql(self, filters: dict, order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count_sql(filters=filters)
            rows = await self.repo.get_list_sql(offset=offset, limit=limit, filters=filters, order=order)

            return total, [EnderecoListItem.model_validate(r) for r in rows]
        except Exception as e:
            app_logger.exception("Erro ao obter endereços %s", e)
            map_data_base_error(e)


    async def get_by_id(self, id: int):
        try:
            r = await self.repo.get_by_id(id)
            if not r:
                return None

            return Endereco.model_validate(r)
        except Exception as e:
            app_logger.exception("Erro ao obter endereço por id %s", e)
            map_data_base_error(e)


    async def create(self, data: dict):
        try:
            r = await self.repo.create(data)
            return Endereco.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def update(self, id: int, data: dict):
        try:
            r = await self.repo.update(id, data)
            if not r:
                return None

            return Endereco.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def delete(self, id: int):
        try:
            r = await self.repo.delete(id)
            if not r:
                return None
            return {"deleted": True}
        except Exception as e:
            map_data_base_error(e)
