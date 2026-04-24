import logging

from app.core.exceptions import CustomException
from app.domain.repositories.endereco_repository import EnderecoRepository
from app.presentation.dtos.endereco_dto import EnderecoDTO
from app.presentation.filters.endereco_filter import EnderecoFilter, EnderecosFilter
from app.presentation.types.helpers.result_type import PaginatedResult

logger = logging.getLogger(__name__)


class EnderecoService:

    def __init__(self, session):
        self.repo: EnderecoRepository = EnderecoRepository(session=session)

    async def get_endereco(self, filtro: EnderecoFilter) -> EnderecoDTO | None:
        try:
            row = await self.repo.get_endereco(filtro=filtro)
            if not row:
                return None

            return EnderecoDTO.model_validate(row)
        except Exception as e:
            logger.exception("Erro get_endereco: %s", e)
            raise CustomException(str(e))

    async def get_enderecos(
        self,
        *,
        filtro: EnderecosFilter,
        offset: int,
        limit: int,
    ) -> PaginatedResult[EnderecoDTO] | None:
        try:
            rows = await self.repo.get_enderecos(
                filtro=filtro,
                offset=offset,
                limit=limit,
            )

            items = [EnderecoDTO.model_validate(row) for row in rows]

            return PaginatedResult(items=items)
        except Exception as e:
            logger.exception("Erro get_enderecos: %s", e)
            raise CustomException(str(e))
