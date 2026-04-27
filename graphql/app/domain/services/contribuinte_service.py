import logging

from app.domain.repositories.contribuinte_repository import ContribuinteRepository
from app.presentation.dtos.contribuinte_dto import ContribuinteDTO
from app.presentation.filters.contribuinte_filter import ContribuinteFilter, ContribuintesFilter

logger = logging.getLogger(__name__)


class ContribuinteService:

    def __init__(self, session):
        self.repo: ContribuinteRepository = ContribuinteRepository(session=session)

    async def get_contribuinte(self, filtro: ContribuinteFilter) -> ContribuinteDTO | None:
        row = await self.repo.get_contribuinte(filtro=filtro)
        if not row:
            return None

        item = ContribuinteDTO.model_validate(row)

        return item

    async def get_contribuintes(
        self,
        *,
        filtro: ContribuintesFilter,
        offset: int,
        limit: int,
    ) -> list[ContribuinteDTO]:
        rows = await self.repo.get_contribuintes(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        items = [ContribuinteDTO.model_validate(row) for row in rows]

        return items
