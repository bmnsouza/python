from datetime import datetime, time
from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.danfe_model import DanfeModel


class DanfeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count()).select_from(DanfeModel)

        if filters:
            for col, val in filters.items():
                if hasattr(DanfeModel, col):
                    q = q.where(getattr(DanfeModel, col) == val)

        result = await self.session.execute(q)
        return int(result.scalar_one())


    async def get_list(self, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None, offset: int = 0, limit: int = 50):
        q = select(DanfeModel)

        if "id_danfe" in filters:
            q = q.where(DanfeModel.id_danfe == filters["id_danfe"])

        if "cd_contribuinte" in filters:
            q = q.where(DanfeModel.cd_contribuinte == filters["cd_contribuinte"])

        if "numero" in filters:
            q = q.where(DanfeModel.numero == filters["numero"])

        if "valor_total" in filters:
            q = q.where(DanfeModel.valor_total >= filters["valor_total"])

        if ("data_emissao_inicio", "data_emissao_fim") in filters:
            q = q.where(DanfeModel.data_emissao >= filters["data_emissao_inicio"])
            q = q.where(DanfeModel.data_emissao <= filters["data_emissao_fim"])

        if order:
            for field, direction in order:
                if hasattr(DanfeModel, field):
                    col = getattr(DanfeModel, field)
                    q = q.order_by(col.asc() if direction == "asc" else col.desc())

        q = q.offset(offset).limit(limit)

        res = await self.session.execute(q)
        return res.scalars().all()


    async def get_by_id(self, id: int):
        q = select(DanfeModel).where(DanfeModel.id_danfe == id)
        res = await self.session.execute(q)
        return res.scalars().first()


    async def create(self, payload: Dict[str, Any]):
        obj = DanfeModel(**payload)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj


    async def update(self, id: int, payload: Dict[str, Any]):
        obj = await self.get_by_id(id)
        if not obj:
            return None

        for k, v in payload.items():
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
