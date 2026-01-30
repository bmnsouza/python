import logging

from typing import Any, Dict, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dto.endereco_dto import EnderecoDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.endereco_repository import EnderecoRepository

logger = logging.getLogger(__name__)


class EnderecoService:
    def __init__(self, session: AsyncSession):
        self.repo = EnderecoRepository(session=session)


    async def get_list(self, filters: dict, order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count_list(filters=filters)
            rows = await self.repo.get_list(offset=offset, limit=limit, filters=filters, order=order)

            return total, [EnderecoDTO.model_validate(r) for r in rows]
        except Exception as e:
            logger.exception("Erro ao obter endereços %s", e)
            map_data_base_error(e)
