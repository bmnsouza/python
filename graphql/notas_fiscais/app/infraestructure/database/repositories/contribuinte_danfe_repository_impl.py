from typing import Any, Dict, List, Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infraestructure.database.query.pagination_builder import build_pagination
from app.presentation.graphql.mappers.pagination_mapper import Pagination


class ContribuinteDanfeRepositoryImpl:

    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filter_monthly(
        self,
        filter: dict
    ) -> Tuple[str, Dict[str, Any]]:
        if not filter:
            return "", {}

        where_clauses: list[str] = []
        params: Dict[str, Any] = {}

        for field, value in filter.items():
            if value is None:
                continue

            if field == "cd_contribuinte":
                where_clauses.append("d.CD_CONTRIBUINTE = :cd_contribuinte")
                params["cd_contribuinte"] = value

            elif field == "year":
                where_clauses.append("EXTRACT(YEAR FROM d.DATA_EMISSAO) = :year")
                params["year"] = value

            elif field == "month":
                where_clauses.append("EXTRACT(MONTH FROM d.DATA_EMISSAO) = :month")
                params["month"] = value

        if not where_clauses:
            return "", {}

        return " WHERE " + " AND ".join(where_clauses), params


    async def count_monthly(
        self,
        filter: dict
    ) -> int:
        where_sql, params = self._apply_filter_monthly(filter=filter)

        sql = text(f"""
            SELECT COUNT(d.ID_DANFE)
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_monthly(
        self,
        *,
        pagination: Pagination,
        filter: dict
    ) -> List[dict]:
        where_sql, params = self._apply_filter_monthly(filter=filter)
        pagination_sql, pagination_params = build_pagination(pagination=pagination)
        params.update(pagination_params)

        sql = text(f"""
            SELECT c.CD_CONTRIBUINTE, c.CNPJ_CONTRIBUINTE, c.NM_FANTASIA, d.NUMERO, d.DATA_EMISSAO, d.VALOR_TOTAL
            FROM NOTA_FISCAL.CONTRIBUINTE c
            JOIN NOTA_FISCAL.DANFE d ON d.CD_CONTRIBUINTE = c.CD_CONTRIBUINTE
            {where_sql}
            ORDER BY d.DATA_EMISSAO DESC
            {pagination_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()
