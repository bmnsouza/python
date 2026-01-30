from typing import Any, Dict, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.presentation.graphql.inputs.contribuinte_input import ContribuinteFilterInput, ContribuinteOrderInput
from app.presentation.graphql.inputs.order_input import OrderDirection


class ContribuinteRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filters_list(self, filter: Optional[ContribuinteFilterInput]) -> Tuple[str, Dict[str, Any]]:
        if not filter:
            return "", {}

        where_clauses = []
        params: Dict[str, Any] = {}

        for field, value in vars(filter).items():
            if value is None:
                continue

            if field == "nm_fantasia" and isinstance(value, str):
                where_clauses.append(f"c.{field} LIKE :{field}")
                params[field] = f"%{value}%"
            else:
                where_clauses.append(f"c.{field} = :{field}")
                params[field] = value

        if not where_clauses:
            return "", {}

        return " WHERE " + " AND ".join(where_clauses), params

    def _apply_order_by_list(self, order: Optional[ContribuinteOrderInput]) -> str:
        if not order:
            return ""

        order_clauses = []

        for field, direction in vars(order).items():
            if direction is None:
                continue

            sql_direction = "ASC" if direction == OrderDirection.ASC else "DESC"
            order_clauses.append(f"c.{field} {sql_direction}")

        if not order_clauses:
            return ""

        return " ORDER BY " + ", ".join(order_clauses)


    async def count_list(self, filter: Optional[ContribuinteFilterInput] = None) -> int:
        where_sql, params = self._apply_filters_list(filter=filter)

        sql = text(f"""
            SELECT COUNT(c.CD_CONTRIBUINTE)
            FROM NOTA_FISCAL.CONTRIBUINTE c
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filter: Optional[ContribuinteFilterInput] = None, order: Optional[ContribuinteOrderInput] = None):
        where_sql, params = self._apply_filters_list(filter=filter)
        order_sql = self._apply_order_by_list(order=order)

        sql = text(f"""
            SELECT c.CD_CONTRIBUINTE, c.CNPJ_CONTRIBUINTE, c.NM_FANTASIA
            FROM NOTA_FISCAL.CONTRIBUINTE c
            {where_sql}
            {order_sql}
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()
