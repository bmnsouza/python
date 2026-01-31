import logging

from typing import List, Optional, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dto.endereco_dto import EnderecoDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.endereco_repository import EnderecoRepository
from app.presentation.graphql.inputs.endereco_input import EnderecoFilterInput, EnderecoOrderInput

logger = logging.getLogger(__name__)


class EnderecoService:
    def __init__(self, session: AsyncSession):
        self.repo = EnderecoRepository(session=session)


    async def get_list(self, offset: int, limit: int, filter: Optional[EnderecoFilterInput], order: Optional[EnderecoOrderInput], ) -> Tuple[int, List[EnderecoDTO]]:
        try:
            total = await self.repo.count_list(filter=filter)
            rows = await self.repo.get_list(offset=offset, limit=limit, filter=filter, order=order)

            return total, [EnderecoDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter endereços %s", e)
            map_data_base_error(e)
