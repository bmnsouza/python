from datetime import datetime, time
from typing import Any, Dict, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.presentation.graphql.inputs.danfe_input import DanfeFilterInput, DanfeFilterLastSevenDaysInput, DanfeFilterMonthlyInput, DanfeOrderInput
from app.presentation.graphql.inputs.order_input import OrderDirection


class DanfeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filter_list(self, filter: Optional[DanfeFilterInput]) -> Tuple[str, Dict[str, Any]]:
        if not filter:
            return "", {}

        where_clauses: list[str] = []
        params: Dict[str, Any] = {}

        for field, value in vars(filter).items():
            if value is None:
                continue

            if field in ("cd_contribuinte", "numero"):
                where_clauses.append(f"d.{field} = :{field}")
                params[field] = value

            elif field == "valor_total":
                where_clauses.append("d.VALOR_TOTAL >= :valor_total")
                params["valor_total"] = value

            elif field == "data_emissao":
                where_clauses.append("d.DATA_EMISSAO BETWEEN :data_inicio AND :data_fim")
                params["data_inicio"] = datetime.combine(value, time.min)
                params["data_fim"] = datetime.combine(value, time.max)

        if not where_clauses:
            return "", {}

        return " WHERE " + " AND ".join(where_clauses), params


    def _apply_order_by_list(self, order: Optional[DanfeOrderInput]) -> str:
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


    async def count_list(self, filter: Optional[DanfeFilterInput] = None) -> int:
        where_sql, params = self._apply_filter_list(filter=filter)

        sql = text(f"""
            SELECT COUNT(d.ID_DANFE)
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filter: Optional[DanfeFilterInput] = None, order: Optional[DanfeOrderInput] = None):
        where_sql, params = self._apply_filter_list(filter=filter)
        order_sql = self._apply_order_by_list(order=order)

        sql = text(f"""
            SELECT d.ID_DANFE, d.CD_CONTRIBUINTE, d.NUMERO, d.VALOR_TOTAL, d.DATA_EMISSAO
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
            {order_sql}
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()


    def _apply_filter_last_seven_days(self, filter: DanfeFilterLastSevenDaysInput) -> Tuple[str, Dict[str, Any]]:
        where_clauses: list[str] = []
        params: Dict[str, Any] = {}

        if filter.cd_contribuinte:
            where_clauses.append("d.CD_CONTRIBUINTE = :cd_contribuinte")
            params["cd_contribuinte"] = filter.cd_contribuinte

        where_clauses.append("TRUNC(d.DATA_EMISSAO) >= TRUNC(SYSDATE) - 7")

        return " WHERE " + " AND ".join(where_clauses), params


    async def count_last_seven_days(self, filter: DanfeFilterLastSevenDaysInput) -> int:
        where_sql, params = self._apply_filter_last_seven_days(filter=filter)

        sql = text(f"""
            SELECT COUNT(d.ID_DANFE)
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_last_seven_days(self, offset: int, limit: int, filter: DanfeFilterLastSevenDaysInput):
        where_sql, params = self._apply_filter_last_seven_days(filter=filter)

        sql = text(f"""
            SELECT d.CD_CONTRIBUINTE, d.NUMERO, d.VALOR_TOTAL, d.DATA_EMISSAO
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
            ORDER BY d.DATA_EMISSAO DESC
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()


    def _apply_filter_monthly(self, filter: DanfeFilterMonthlyInput) -> Tuple[str, Dict[str, Any]]:
        if not filter:
            return "", {}

        where_clauses: list[str] = []
        params: Dict[str, Any] = {}

        for field, value in vars(filter).items():
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


    async def count_monthly(self, filter: DanfeFilterMonthlyInput) -> int:
        where_sql, params = self._apply_filter_monthly(filter=filter)

        sql = text(f"""
            SELECT COUNT(d.ID_DANFE)
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_monthly(self, offset: int, limit: int, filter: DanfeFilterMonthlyInput):
        where_sql, params = self._apply_filter_monthly(filter=filter)

        sql = text(f"""
            SELECT d.NUMERO, d.VALOR_TOTAL, d.DATA_EMISSAO
            FROM NOTA_FISCAL.DANFE d
            {where_sql}
            ORDER BY d.DATA_EMISSAO DESC
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()
