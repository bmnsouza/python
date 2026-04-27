import logging

from app.domain.repositories.danfe_repository import DanfeRepository
from app.presentation.dtos.danfe_dto import DanfeDTO
from app.presentation.filters.danfe_filter import DanfeFilter, DanfesFilter

logger = logging.getLogger(__name__)


class DanfeService:

    def __init__(self, session):
        self.repo: DanfeRepository = DanfeRepository(session=session)

    async def get_danfe(self, filtro: DanfeFilter) -> DanfeDTO | None:
        row = await self.repo.get_danfe(filtro=filtro)
        if not row:
            return None

        item = DanfeDTO.model_validate(row)

        return item

    async def get_danfes(
        self,
        *,
        filtro: DanfesFilter,
        offset: int,
        limit: int,
    ) -> list[DanfeDTO]:
        rows = await self.repo.get_danfes(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        items = [DanfeDTO.model_validate(row) for row in rows]

        return items
