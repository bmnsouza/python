import logging

from typing import List, Tuple

from app.application.dto.endereco_dto import EnderecoListDTO
from app.core.exception import map_data_base_error
from app.domain.repositories.endereco_repository import EnderecoRepository
from app.presentation.graphql.mappers.pagination_mapper import Pagination

logger = logging.getLogger(__name__)


class EnderecoService:

    def __init__(self, repo: EnderecoRepository):
        self.repo = repo


    async def get_list(
        self,
        *,
        pagination: Pagination,
        filter: dict | None,
        order: dict | None
    ) -> Tuple[int, List[EnderecoListDTO]]:
        try:
            total = await self.repo.count_list(filter=filter)
            rows = await self.repo.get_list(
                pagination=pagination,
                filter=filter,
                order=order
            )

            return total, [
                EnderecoListDTO.model_validate(row)
                for row in rows
            ]

        except Exception as e:
            logger.exception("Erro ao obter endereços %s", e)
            map_data_base_error(e)
