import logging

from typing import List, Optional, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dto.danfe_dto import DanfeDTO, DanfeLastSevenDaysDTO, DanfeMonthlyDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.danfe_repository import DanfeRepository
from app.presentation.graphql.inputs.danfe_input import DanfeFilterInput, DanfeFilterLastSevenDaysInput, DanfeFilterMonthlyInput, DanfeOrderInput

logger = logging.getLogger(__name__)


class DanfeService:
    def __init__(self, session: AsyncSession):
        self.repo = DanfeRepository(session=session)


    async def get_list(self, offset: int, limit: int, filter: Optional[DanfeFilterInput], order: Optional[DanfeOrderInput]) -> Tuple[int, List[DanfeDTO]]:
        try:
            total = await self.repo.count_list(filter=filter)
            rows = await self.repo.get_list(offset=offset, limit=limit, filter=filter, order=order)

            return total, [DanfeDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_last_seven_days(self, offset: int, limit: int, filter: DanfeFilterLastSevenDaysInput) -> Tuple[int, List[DanfeLastSevenDaysDTO]]:
        try:
            total = await self.repo.count_last_seven_days(filter=filter)
            rows = await self.repo.get_last_seven_days(offset=offset, limit=limit, filter=filter)

            return total, [DanfeLastSevenDaysDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_monthly(self, offset: int, limit: int, filter: DanfeFilterMonthlyInput) -> Tuple[int, List[DanfeMonthlyDTO]]:
        try:
            total = await self.repo.count_monthly(filter=filter)
            rows = await self.repo.get_monthly(offset=offset, limit=limit, filter=filter)

            return total, [DanfeMonthlyDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)
