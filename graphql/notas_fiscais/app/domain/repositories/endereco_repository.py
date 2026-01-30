from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infraestructure.database.models.endereco_model import EnderecoModel


class EnderecoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filters_list(self, filters: Optional[Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
        where = []
        params = {}

        if filters:
            for col, val in filters.items():
                if not hasattr(EnderecoModel, col):
                    continue

                if isinstance(val, str) and col.lower() in ("logradouro", "municipio"):
                    where.append(f"{col} LIKE :{col}")
                    params[col] = f"%{val}%"
                else:
                    where.append(f"{col} = :{col}")
                    params[col] = val

        if not where:
            return "", params

        return " WHERE " + " AND ".join(where), params


    async def count_list(self, filters: Optional[Dict[str, Any]] = None) -> int:
        where_sql, params = self._apply_filters_list(filters=filters)

        sql = text(f"""
            SELECT COUNT(ID_ENDERECO)
            FROM NOTA_FISCAL.ENDERECO
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None):
        where_sql, params = self._apply_filters_list(filters=filters)

        order_sql = ""
        if order:
            order_clauses = []
            for field, direction in order:
                if field in EnderecoModel.__table__.columns:
                    order_sql = "ASC" if direction.lower() == "asc" else "DESC"
                    order_clauses.append(f"{field} {order_sql}")

            if order_clauses:
                order_sql = " ORDER BY " + ", ".join(order_clauses)

        sql = text(f"""
            SELECT ID_ENDERECO, CD_CONTRIBUINTE, LOGRADOURO, MUNICIPIO, UF
            FROM NOTA_FISCAL.ENDERECO
            {where_sql}
            {order_sql}
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()
