import logging

from typing import List, Tuple

from app.application.dto.contribuinte_danfe_dto import ContribuinteDanfeMonthlyDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.contribuinte_danfe_repository import ContribuinteDanfeRepository
from app.presentation.graphql.mappers.pagination_mapper import Pagination

logger = logging.getLogger(__name__)


class ContribuinteDanfeService:

    def __init__(self, repo: ContribuinteDanfeRepository):
        self.repo = repo


    async def get_monthly(
        self,
        *,
        pagination: Pagination,
        filter: dict
    ) -> Tuple[int, List[ContribuinteDanfeMonthlyDTO]]:
        try:
            total = await self.repo.count_monthly(filter=filter)
            rows = await self.repo.get_monthly(
                pagination=pagination,
                filter=filter
            )

            return total, [
                ContribuinteDanfeMonthlyDTO.model_validate(row)
                for row in rows
            ]

        except Exception as e:
            logger.exception("Erro ao obter dados do contribuinte com os danfes %s", e)
            map_data_base_error(e)
