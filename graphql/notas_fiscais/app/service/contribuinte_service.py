from typing import Any, Dict, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logger import app_logger
from app.fastapi.schema.contribuinte_schema import Contribuinte
from app.repository.contribuinte_repository import ContribuinteRepository
from app.utils.error_util import map_data_base_error


class ContribuinteService:
    def __init__(self, session: AsyncSession):
        self.repo = ContribuinteRepository(session=session)


    async def get_list(self, filters: dict, order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count(filters=filters)
            rows = await self.repo.get_list(offset=offset, limit=limit, filters=filters, order=order)

            return total, [Contribuinte.model_validate(r) for r in rows]
        except Exception as e:
            app_logger.exception("Erro ao obter contribuintes %s", e)
            map_data_base_error(e)


    async def get_list_sql(self, filters: dict, order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count_sql(filters=filters)
            rows = await self.repo.get_list_sql(offset=offset, limit=limit, filters=filters, order=order)

            return total, [Contribuinte.model_validate(r) for r in rows]
        except Exception as e:
            app_logger.exception("Erro ao obter contribuintes %s", e)
            map_data_base_error(e)


    async def get_by_cd(self, cd: str):
        try:
            r = await self.repo.get_by_cd(cd=cd)
            if not r:
                return None

            return Contribuinte.model_validate(r)
        except Exception as e:
            app_logger.exception("Erro ao obter contribuinte por cd %s", e)
            map_data_base_error(e)


    async def create(self, data: dict):
        try:
            r = await self.repo.create(data)
            return Contribuinte.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def update(self, cd: str, data: dict):
        try:
            r = await self.repo.update(cd, data)
            if not r:
                return None

            return Contribuinte.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def delete(self, cd: str):
        try:
            r = await self.repo.delete(cd)
            if not r:
                return None
            return {"deleted": True}
        except Exception as e:
            map_data_base_error(e)
