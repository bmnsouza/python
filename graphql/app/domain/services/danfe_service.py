import logging

from app.core.exceptions import CustomException
from app.presentation.dtos.danfe_dto import DanfeDTO
from app.presentation.filters.danfe_filter import DanfeFilter, DanfesFilter
from app.presentation.types.helpers.result_type import PaginatedResult

from ..repositories.danfe_repository import DanfeRepository

logger = logging.getLogger(__name__)


class DanfeService:

    def __init__(self, session):
        self.repo: DanfeRepository = DanfeRepository(session=session)

    async def get_danfe(self, filtro: DanfeFilter) -> DanfeDTO | None:
        try:
            row = await self.repo.get_danfe(filtro=filtro)
            if not row:
                return None

            return DanfeDTO.model_validate(row)
        except Exception as e:
            logger.exception("Erro get_danfe: %s", e)
            raise CustomException(str(e))

    async def get_danfes(
        self,
        *,
        filtro: DanfesFilter,
        offset: int,
        limit: int,
    ) -> PaginatedResult[DanfeDTO] | None:
        try:
            rows = await self.repo.get_danfes(
                filtro=filtro,
                offset=offset,
                limit=limit,
            )

            items = [DanfeDTO.model_validate(row) for row in rows]

            return PaginatedResult(items=items)
        except Exception as e:
            logger.exception("Erro get_danfes: %s", e)
            raise CustomException(str(e))
