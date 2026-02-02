from typing import Any, Dict, Tuple, List

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infraestructure.database.query.order_by_builder import build_order_by
from app.infraestructure.database.query.pagination_builder import build_pagination
from app.presentation.graphql.mappers.pagination_mapper import Pagination


class ContribuinteRepositoryImpl:

    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filter_list(
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

            if field == "nm_fantasia":
                where_clauses.append("c.NM_FANTASIA LIKE :nm_fantasia")
                params["nm_fantasia"] = f"%{value}%"
            else:
                where_clauses.append(f"c.{field} = :{field}")
                params[field] = value

        if not where_clauses:
            return "", {}

        return " WHERE " + " AND ".join(where_clauses), params


    async def count_list(
        self,
        filter: dict | None = None
    ) -> int:
        where_sql, params = self._apply_filter_list(filter=filter)

        sql = text(f"""
            SELECT COUNT(c.CD_CONTRIBUINTE)
            FROM NOTA_FISCAL.CONTRIBUINTE c
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(
        self,
        *,
        pagination: Pagination,
        filter: dict | None = None,
        order: dict | None = None
    ) -> List[dict]:
        where_sql, params = self._apply_filter_list(filter=filter)
        order_sql = build_order_by(order=order)
        pagination_sql, pagination_params = build_pagination(pagination=pagination)
        params.update(pagination_params)

        sql = text(f"""
            SELECT c.CD_CONTRIBUINTE, c.CNPJ_CONTRIBUINTE, c.NM_FANTASIA
            FROM NOTA_FISCAL.CONTRIBUINTE c
            {where_sql}
            {order_sql}
            {pagination_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()
