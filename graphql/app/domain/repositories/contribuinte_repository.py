from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.builders.contribuinte_builder import ContribuinteBuilder
from app.presentation.filters.contribuinte_filter import ContribuinteFilter, ContribuintesFilter


class ContribuinteRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_contribuinte(self, filtro: ContribuinteFilter) -> dict[str, Any] | None:
        statement, parameters = ContribuinteBuilder.Contribuinte.build_statement(filtro=filtro)

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().first()

    async def get_contribuintes(
        self,
        *,
        filtro: ContribuintesFilter,
        offset: int,
        limit: int,
    ) -> list[dict[str, Any]] | None:
        statement, parameters = ContribuinteBuilder.Contribuintes.build_statement(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().all()
