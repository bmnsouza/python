from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.builders.danfe_builder import DanfeBuilder
from app.presentation.filters.danfe_filter import DanfesFilter


class DanfeRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_danfes_json_banco(
        self,
        *,
        filtro: DanfesFilter,
        offset: int,
        limit: int,
    ) -> list[dict[str, Any]] | None:
        statement, parameters = DanfeBuilder.DanfesJsonBanco.build_statement(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().all()

    async def get_danfes_json_python(
        self,
        *,
        filtro: DanfesFilter,
        offset: int,
        limit: int,
    ) -> list[dict[str, Any]] | None:
        statement, parameters = DanfeBuilder.DanfesJsonPython.build_statement(
            filtro=filtro,
            offset=offset,
            limit=limit,
        )

        result = await self.session.execute(statement=statement, params=parameters)
        return result.mappings().all()
