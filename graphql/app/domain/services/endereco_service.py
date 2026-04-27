import logging

from app.domain.repositories.endereco_repository import EnderecoRepository
from app.presentation.dtos.endereco_dto import EnderecoDTO
from app.presentation.filters.endereco_filter import EnderecoFilter, EnderecosFilter

logger = logging.getLogger(__name__)


class EnderecoService:

    def __init__(self, session):
        self.repo: EnderecoRepository = EnderecoRepository(session=session)

    async def get_endereco(self, filtro: EnderecoFilter) -> EnderecoDTO | None:
        row = await self.repo.get_endereco(filtro=filtro)
        if not row:
            return None

        item = EnderecoDTO.model_validate(row)

        return item

    async def get_enderecos(
        self,
        *,
        filtro: EnderecosFilter,
        offset: int,
        limit: int,
    ) -> list[EnderecoDTO]:
        rows = await self.repo.get_enderecos(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        items = [EnderecoDTO.model_validate(row) for row in rows]

        return items
