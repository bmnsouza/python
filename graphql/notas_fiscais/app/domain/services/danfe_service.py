import logging

from typing import List, Tuple

from app.application.dto.danfe_dto import DanfeListDTO, DanfeLastSevenDaysDTO, DanfeMonthlyDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.danfe_repository import DanfeRepository
from app.presentation.graphql.mappers.pagination_mapper import Pagination

logger = logging.getLogger(__name__)


class DanfeService:

    def __init__(self, repo: DanfeRepository):
        self.repo = repo


    async def get_list(
        self,
        *,
        pagination: Pagination,
        filter: dict | None = None,
        order: dict | None = None
    ) -> Tuple[int, List[DanfeListDTO]]:
        try:
            total = await self.repo.count_list(filter=filter)
            rows = await self.repo.get_list(
                pagination=pagination,
                filter=filter,
                order=order
            )

            return total, [
                DanfeListDTO.model_validate(row)
                for row in rows
            ]

        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_last_seven_days(
        self,
        *,
        pagination: Pagination,
        filter: dict
    ) -> Tuple[int, List[DanfeLastSevenDaysDTO]]:
        try:
            total = await self.repo.count_last_seven_days(filter=filter)
            rows = await self.repo.get_last_seven_days(
                pagination=pagination,
                filter=filter
            )

            return total, [
                DanfeLastSevenDaysDTO.model_validate(row)
                for row in rows
            ]

        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_monthly(
        self,
        *,
        pagination: Pagination,
        filter: dict
    ) -> Tuple[int, List[DanfeMonthlyDTO]]:
        try:
            total = await self.repo.count_monthly(filter=filter)
            rows = await self.repo.get_monthly(
                pagination=pagination,
                filter=filter
            )

            return total, [
                DanfeMonthlyDTO.model_validate(row)
                for row in rows
            ]

        except Exception as e:
            logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)
