from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.builders.endereco_builder import EnderecoBuilder
from app.presentation.filters.endereco_filter import EnderecoFilter, EnderecosFilter


class EnderecoRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_endereco(self, filtro: EnderecoFilter) -> dict[str, Any] | None:
        statement, parameters = EnderecoBuilder.Endereco.build_statement(filtro=filtro)

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().first()

    async def get_enderecos(
        self,
        *,
        filtro: EnderecosFilter,
        offset: int,
        limit: int,
    ) -> list[dict[str, Any]] | None:
        statement, parameters = EnderecoBuilder.Enderecos.build_statement(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().all()
