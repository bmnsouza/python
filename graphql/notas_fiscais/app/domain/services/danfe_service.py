import logging

from typing import Any, Dict, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dto.danfe_dto import DanfeDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.danfe_repository import DanfeRepository

logger = logging.getLogger(__name__)


class DanfeService:
    def __init__(self, session: AsyncSession):
        self.repo = DanfeRepository(session=session)


    async def get_list(self, filters: dict, order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count_list(filters=filters)
            rows = await self.repo.get_list(offset=offset, limit=limit, filters=filters, order=order)

            return total, [DanfeDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_last_seven_days(self, cd_contribuinte: str, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count_last_seven_days(cd_contribuinte=cd_contribuinte)
            rows = await self.repo.get_last_seven_days(offset=offset, limit=limit, cd_contribuinte=cd_contribuinte)

            return total, [DanfeDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_monthly(self, filters: dict, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count_monthly(filters=filters)
            rows = await self.repo.get_monthly(offset=offset, limit=limit, filters=filters)

            return total, [DanfeDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)
