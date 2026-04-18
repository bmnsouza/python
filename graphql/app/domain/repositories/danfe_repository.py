from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.builders.danfe_builder import DanfeBuilder
from app.presentation.filters.danfe_filter import DanfeFilter, DanfesFilter


class DanfeRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_danfe(self, filtro: DanfeFilter) -> dict[str, Any] | None:
        statement, parameters = DanfeBuilder.Danfe.build_statement(filtro=filtro)

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().first()

    async def get_danfes(
        self,
        *,
        filtro: DanfesFilter,
        offset: int,
        limit: int,
    ) -> list[dict[str, Any]] | None:
        statement, parameters = DanfeBuilder.Danfes.build_statement(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().all()
