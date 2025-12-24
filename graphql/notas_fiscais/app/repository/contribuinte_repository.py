from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.model.contribuinte_model import ContribuinteModel


class ContribuinteRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filters(self, q, filters: dict):
        if filters:
            for col, val in filters.items():
                if hasattr(ContribuinteModel, col):
                    col_attr = getattr(ContribuinteModel, col)

                    if isinstance(val, str) and col.lower() == "nm_fantasia":
                        q = q.where(col_attr.ilike(f"%{val}%"))
                    else:
                        q = q.where(col_attr == val)
        return q


    def _apply_filters_sql(self, filters: Optional[Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
        where = []
        params = {}

        if filters:
            for col, val in filters.items():
                if not hasattr(ContribuinteModel, col):
                    continue

                if isinstance(val, str) and col.lower() == "nm_fantasia":
                    where.append(f"{col} LIKE :{col}")
                    params[col] = f"%{val}%"
                else:
                    where.append(f"{col} = :{col}")
                    params[col] = val

        if not where:
            return "", params

        return " WHERE " + " AND ".join(where), params


    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count(ContribuinteModel.cd_contribuinte))
        q = self._apply_filters(q=q, filters=filters)

        result = await self.session.execute(q)
        return result.scalar_one()


    async def count_sql(self, filters: Optional[Dict[str, Any]] = None) -> int:
        where_sql, params = self._apply_filters_sql(filters=filters)

        sql = text(f"""
            SELECT COUNT(CD_CONTRIBUINTE)
            FROM NOTA_FISCAL.CONTRIBUINTE
            {where_sql}
        """)

        result = await self.session.execute(statement=sql, params=params)
        return result.scalar_one()


    async def get_list(self, offset: int, limit: int, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None):
        q = (
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.enderecos),
                selectinload(ContribuinteModel.danfes),
            )
        )

        q = self._apply_filters(q, filters)

        if order:
            for field, direction in order:
                if hasattr(ContribuinteModel, field):
                    col = getattr(ContribuinteModel, field)
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
                if hasattr(ContribuinteModel, field):
                    order_sql = "ASC" if direction.lower() == "asc" else "DESC"
                    order_clauses.append(f"{field} {order_sql}")

            if order_clauses:
                order_sql = " ORDER BY " + ", ".join(order_clauses)

        sql = text(f"""
            SELECT CD_CONTRIBUINTE, CNPJ_CONTRIBUINTE, NM_FANTASIA
            FROM NOTA_FISCAL.CONTRIBUINTE
            {where_sql}
            {order_sql}
            OFFSET :offset ROWS
            FETCH NEXT :limit ROWS ONLY
        """)

        params.update({"offset": offset, "limit": limit})

        result = await self.session.execute(statement=sql, params=params)
        return result.mappings().all()


    async def get_by_cd(self, cd: str):
        q = select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd)
        res = await self.session.execute(q)
        return res.scalars().first()


    async def create(self, data: dict):
        obj = ContribuinteModel(**data)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj


    async def update(self, cd: str, data: dict):
        obj = await self.get_by_cd(cd)
        if not obj:
            return None

        for k, v in data.items():
            if hasattr(obj, k):
                setattr(obj, k, v)

        await self.session.commit()
        await self.session.refresh(obj)
        return obj


    async def delete(self, cd: str):
        obj = await self.get_by_cd(cd)
        if not obj:
            return None

        await self.session.delete(obj)
        await self.session.commit()
        return obj
