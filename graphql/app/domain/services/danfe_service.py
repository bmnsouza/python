import logging

from app.application.dtos.danfe_dto import DanfeDTO
from app.application.mappers.danfe_mapper import DanfeMapper
from app.domain.repositories.danfe_repository import DanfeRepository
from app.presentation.filters.danfe_filter import DanfesFilter

logger = logging.getLogger(__name__)


class DanfeService:

    def __init__(self, session):
        self.repo: DanfeRepository = DanfeRepository(session=session)

    async def get_danfes_json_banco(self, *, filtro: DanfesFilter, offset: int, limit: int) -> list[DanfeDTO]:
        rows = await self.repo.get_danfes_json_banco(filtro=filtro, offset=offset, limit=limit)
        return [DanfeDTO.model_validate(row) for row in rows]

    async def get_danfes_json_python(self, *, filtro: DanfesFilter, offset: int, limit: int) -> list[DanfeDTO]:
        rows = await self.repo.get_danfes_json_python(filtro=filtro, offset=offset, limit=limit)
        return DanfeMapper.agrupar(rows)
