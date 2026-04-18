import logging

from app.core.exceptions import CustomException
from app.presentation.dtos.contribuinte_dto import ContribuinteDTO
from app.presentation.filters.contribuinte_filter import ContribuinteFilter, ContribuintesFilter
from app.presentation.types.helpers.result_type import PaginatedResult

from ..repositories.contribuinte_repository import ContribuinteRepository

logger = logging.getLogger(__name__)


class ContribuinteService:

    def __init__(self, session):
        self.repo: ContribuinteRepository = ContribuinteRepository(session=session)

    async def get_contribuinte(self, filtro: ContribuinteFilter) -> ContribuinteDTO | None:
        try:
            row = await self.repo.get_contribuinte(filtro=filtro)
            if not row:
                return None

            return ContribuinteDTO.model_validate(row)
        except Exception as e:
            logger.exception("Erro get_contribuinte: %s", e)
            raise CustomException(str(e))

    async def get_contribuintes(
        self,
        *,
        filtro: ContribuintesFilter,
        offset: int,
        limit: int,
    ) -> PaginatedResult[ContribuinteDTO] | None:
        try:
            rows = await self.repo.get_contribuintes(
                filtro=filtro,
                offset=offset,
                limit=limit,
            )

            items = [ContribuinteDTO.model_validate(row) for row in rows]

            return PaginatedResult(items=items)
        except Exception as e:
            logger.exception("Erro get_contribuintes: %s", e)
            raise CustomException(str(e))
