from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.endereco_model import EnderecoModel


class EnderecoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    def _apply_filters(self, q, filters: Dict[str, Any]):
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


    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count(EnderecoModel.id_endereco))
        q = self._apply_filters(q, filters)

        result = await self.session.execute(q)
        return result.scalar_one()


    async def get_list(self, filters: Optional[Dict[str, Any]] = None, order: Optional[List[Tuple[str, str]]] = None, offset: int = 0, limit: int = 50):
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


    async def get_by_id(self, id: int):
        q = select(EnderecoModel).where(EnderecoModel.id_endereco == id)
        res = await self.session.execute(q)
        return res.scalars().first()


    async def create(self, payload: Dict[str, Any]):
        obj = EnderecoModel(**payload)
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
