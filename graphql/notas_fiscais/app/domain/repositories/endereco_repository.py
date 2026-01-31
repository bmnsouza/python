from typing import Any, Dict, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infraestructure.database.query.order_by_builder import build_order_by
from app.infraestructure.database.query.pagination_builder import build_pagination
from app.presentation.graphql.inputs.endereco_input import EnderecoFilterInput, EnderecoOrderInput


class EnderecoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filter_list(self, filter: Optional[EnderecoFilterInput]) -> Tuple[str, Dict[str, Any]]:
        if not filter:
            return "", {}

        where_clauses: list[str] = []
        params: Dict[str, Any] = {}

        for field, value in vars(filter).items():
            if value is None:
                continue

            if field in ("logradouro", "municipio"):
                where_clauses.append(f"e.{field} LIKE :{field}")
                params[field] = f"%{value}%"
            else:
                where_clauses.append(f"e.{field} = :{field}")
                params[field] = value

        if not where_clauses:
            return "", {}

        return " WHERE " + " AND ".join(where_clauses), params


    async def count_list(self, filter: Optional[EnderecoFilterInput] = None) -> int:
        where_sql, params = self._apply_filter_list(filter=filter)

        sql = text(f"""
            SELECT COUNT(e.ID_ENDERECO)
            FROM NOTA_FISCAL.ENDERECO e
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filter: Optional[EnderecoFilterInput] = None, order: Optional[EnderecoOrderInput] = None):
        where_sql, params = self._apply_filter_list(filter=filter)
        order_sql = build_order_by(order=order)
        pagination_sql, pagination_params = build_pagination(offset=offset, limit=limit)
        params.update(pagination_params)

        sql = text(f"""
            SELECT e.ID_ENDERECO, e.CD_CONTRIBUINTE, e.LOGRADOURO, e.MUNICIPIO, e.UF
            FROM NOTA_FISCAL.ENDERECO e
            {where_sql}
            {order_sql}
            {pagination_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()
