from datetime import datetime, time
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.danfe_model import DanfeModel


class DanfeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filters(self, q, filters: dict):
        if "id_danfe" in filters:
            q = q.where(DanfeModel.id_danfe == filters["id_danfe"])

        if "cd_contribuinte" in filters:
            q = q.where(DanfeModel.cd_contribuinte == filters["cd_contribuinte"])

        if "numero" in filters:
            q = q.where(DanfeModel.numero == filters["numero"])

        if "valor_total" in filters:
            q = q.where(DanfeModel.valor_total >= filters["valor_total"])

        if "data_emissao" in filters:
            dt = filters["data_emissao"]
            start = datetime.combine(dt, time.min)
            end = datetime.combine(dt, time.max)

            q = q.where(DanfeModel.data_emissao.between(start, end))

        return q


    def _apply_filters_sql(self, filters: Optional[Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
        where = []
        params = {}

        if filters:
            if "id_danfe" in filters:
                where.append("id_danfe = :id_danfe")
                params["id_danfe"] = filters["id_danfe"]

            if "cd_contribuinte" in filters:
                where.append("cd_contribuinte = :cd_contribuinte")
                params["cd_contribuinte"] = filters["cd_contribuinte"]

            if "numero" in filters:
                where.append("numero = :numero")
                params["numero"] = filters["numero"]

            if "valor_total" in filters:
                where.append("valor_total >= :valor_total")
                params["valor_total"] = filters["valor_total"]

            if "data_emissao" in filters:
                dt = filters["data_emissao"]
                start = datetime.combine(dt, time.min)
                end = datetime.combine(dt, time.max)

                where.append("data_emissao BETWEEN TO_DATE(:start, 'yyyy-mm-dd hh24:mi:ss') AND TO_DATE(:end, 'yyyy-mm-dd hh24:mi:ss')")
                params["start"] = start
                params["end"] = end

        if not where:
            return "", params

        return " WHERE " + " AND ".join(where), params


    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count(DanfeModel.id_danfe))
        q = self._apply_filters(q, filters)

        result = await self.session.execute(q)
        return result.scalar_one()


    async def count_sql(self, filters: Optional[Dict[str, Any]] = None) -> int:
        where_sql, params = self._apply_filters_sql(filters=filters)

        sql = text(f"""
            SELECT COUNT(ID_DANFE)
            FROM NOTA_FISCAL.DANFE
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None):
        q = select(DanfeModel)
        q = self._apply_filters(q, filters)

        if order:
            for field, direction in order:
                if hasattr(DanfeModel, field):
                    col = getattr(DanfeModel, field)
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
                if field in DanfeModel.__table__.columns:
                    order_sql = "ASC" if direction.lower() == "asc" else "DESC"
                    order_clauses.append(f"{field} {order_sql}")

            if order_clauses:
                order_sql = " ORDER BY " + ", ".join(order_clauses)

        sql = text(f"""
            SELECT ID_DANFE, CD_CONTRIBUINTE, NUMERO, VALOR_TOTAL, DATA_EMISSAO
            FROM NOTA_FISCAL.DANFE
            {where_sql}
            {order_sql}
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()


    async def get_by_id(self, id: int):
        q = select(DanfeModel).where(DanfeModel.id_danfe == id)
        res = await self.session.execute(q)
        return res.scalars().first()


    async def create(self, data: dict):
        obj = DanfeModel(**data)
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
