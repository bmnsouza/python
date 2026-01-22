from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.endereco_model import EnderecoModel


class EnderecoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filters(self, q, filters: dict):
        if filters:
            for col, val in filters.items():
                if hasattr(EnderecoModel, col):
                    col_attr = getattr(EnderecoModel, col)

                    if isinstance(val, str) and "%" in val:
                        q = q.where(col_attr.like(val))
                    elif isinstance(val, str) and col.lower() in ("logradouro", "municipio"):
                        q = q.where(col_attr.ilike(f"%{val}%"))
                    else:
                        q = q.where(col_attr == val)
        return q


    def _apply_filters_sql(self, filters: Optional[Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
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


    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count(EnderecoModel.id_endereco))
        q = self._apply_filters(q, filters)

        result = await self.session.execute(q)
        return result.scalar_one()


    async def count_sql(self, filters: Optional[Dict[str, Any]] = None) -> int:
        where_sql, params = self._apply_filters_sql(filters=filters)

        sql = text(f"""
            SELECT COUNT(ID_ENDERECO)
            FROM NOTA_FISCAL.ENDERECO
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None):
        q = select(EnderecoModel)
        q = self._apply_filters(q, filters)

        if order:
            for field, direction in order:
                if hasattr(EnderecoModel, field):
                    col = getattr(EnderecoModel, field)
                    q = q.order_by(col.asc() if direction == "asc" else col.desc())

        q = q.offset(offset).limit(limit)

        result = await self.session.execute(q)
        return result.scalars().all()


    async def get_list_sql(self, offset: int, limit: int, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None):
        where_sql, params = self._apply_filters_sql(filters=filters)

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


    async def get_by_id(self, id: int):
        q = select(EnderecoModel).where(EnderecoModel.id_endereco == id)
        res = await self.session.execute(q)
        return res.scalars().first()


    async def create(self, data: dict):
        obj = EnderecoModel(**data)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj


    async def update(self, id: int, data: dict):
        obj = await self.get_by_id(id)
        if not obj:
            return None

        for k, v in data.items():
            if hasattr(obj, k):
                setattr(obj, k, v)

        await self.session.commit()
        await self.session.refresh(obj)
        return obj


    async def delete(self, id: int):
        obj = await self.get_by_id(id)
        if not obj:
            return None

        await self.session.delete(obj)
        await self.session.commit()
        return obj
