from typing import Any, Dict, List, Optional, Tuple
from sqlalchemy import select, func, literal_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.model.contribuinte_model import ContribuinteModel


class ContribuinteRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    # ---------------------------------------------------------------------
    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count()).select_from(ContribuinteModel)

        if filters:
            for col, val in filters.items():
                if hasattr(ContribuinteModel, col):
                    q = q.where(getattr(ContribuinteModel, col) == val)

        result = await self.session.execute(q)
        return int(result.scalar_one())

    # ---------------------------------------------------------------------
    async def list(
        self,
        filters: Optional[Dict[str, Any]] = None,
        order: Optional[List[Tuple[str, str]]] = None,
        offset: int = 0,
        limit: int = 50,
    ):
        q = (
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.enderecos),
                selectinload(ContribuinteModel.danfes),
            )
        )

        if filters:
            for col, val in filters.items():
                if hasattr(ContribuinteModel, col):
                    col_attr = getattr(ContribuinteModel, col)

                    if isinstance(val, str) and "%" in val:
                        q = q.where(col_attr.like(val))
                    elif isinstance(val, str) and col.lower() in ("nm_fantasia", "nome"):
                        q = q.where(col_attr.ilike(f"%{val}%"))
                    else:
                        q = q.where(col_attr == val)

        if order:
            for field, direction in order:
                if hasattr(ContribuinteModel, field):
                    col = getattr(ContribuinteModel, field)
                    q = q.order_by(col.asc() if direction == "asc" else col.desc())

        q = q.offset(offset).limit(limit)

        res = await self.session.execute(q)
        return res.scalars().all()

    # ---------------------------------------------------------------------
    async def get_by_cd(self, cd: str):
        q = select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd)
        res = await self.session.execute(q)
        return res.scalars().first()

    # ---------------------------------------------------------------------
    async def get_by_cnpj(self, cnpj: str):
        q = select(ContribuinteModel).where(ContribuinteModel.cnpj_contribuinte == cnpj)
        res = await self.session.execute(q)
        return res.scalars().first()

    # ---------------------------------------------------------------------
    async def create(self, payload: Dict[str, Any]):
        obj = ContribuinteModel(**payload)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    # ---------------------------------------------------------------------
    async def update(self, cd: str, payload: Dict[str, Any]):
        obj = await self.get_by_cd(cd)
        if not obj:
            return None

        for k, v in payload.items():
            if hasattr(obj, k):
                setattr(obj, k, v)

        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    # ---------------------------------------------------------------------
    async def delete(self, cd: str):
        obj = await self.get_by_cd(cd)
        if not obj:
            return None

        await self.session.delete(obj)
        return obj
