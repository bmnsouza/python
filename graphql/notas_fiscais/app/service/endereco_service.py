from typing import Any, Dict, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logger import app_logger
from app.fastapi.schema.endereco_schema import Endereco
from app.repository.endereco_repository import EnderecoRepository
from app.utils.error_util import map_data_base_error


class EnderecoService:
    def __init__(self, session: AsyncSession):
        self.repo = EnderecoRepository(session=session)


    async def get_list(self, filters: Dict[str, Any], order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count(filters)
            rows = await self.repo.get_list(filters, order, offset, limit)

            return total, [Endereco.model_validate(r) for r in rows]
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


    async def create(self, payload: Dict[str, Any]):
        try:
            r = await self.repo.create(payload)
            return Endereco.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def update(self, id: int, payload: Dict[str, Any]):
        try:
            r = await self.repo.update(id, payload)
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
