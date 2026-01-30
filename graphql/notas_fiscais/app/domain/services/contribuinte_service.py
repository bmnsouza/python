import logging

from typing import List, Optional, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dto.contribuinte_dto import ContribuinteDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.contribuinte_repository import ContribuinteRepository
from app.presentation.graphql.inputs.contribuinte_input import ContribuinteFilterInput, ContribuinteOrderInput

logger = logging.getLogger(__name__)


class ContribuinteService:
    def __init__(self, session: AsyncSession):
        self.repo = ContribuinteRepository(session=session)


    async def get_list(self, offset: int, limit: int, filter: Optional[ContribuinteFilterInput], order: Optional[ContribuinteOrderInput]) -> Tuple[int, List[ContribuinteDTO]]:
        try:
            total = await self.repo.count_list(filter=filter)
            rows = await self.repo.get_list(offset=offset, limit=limit, filter=filter, order=order)

            return total, [ContribuinteDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter contribuintes %s", e)
            map_data_base_error(e)
