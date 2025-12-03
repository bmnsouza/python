# app/repository/contribuinte_repository.py
from typing import Any, Dict, List, Optional, Tuple
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.model.contribuinte_model import ContribuinteModel


class ContribuinteRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        q = select(func.count(ContribuinteModel.cd_contribuinte))
        if filters:
            for col, val in filters.items():
                if hasattr(ContribuinteModel, col):
                    col_attr = getattr(ContribuinteModel, col)
                    q = q.where(col_attr == val)
        result = await self.session.execute(q)
        return int(result.scalar_one())

    async def list(
        self,
        filters: Optional[Dict[str, Any]] = None,
        order: Optional[List[Tuple[str, str]]] = None,
        offset: int = 0,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        q = select(ContribuinteModel).options(
            selectinload(ContribuinteModel.enderecos),
            selectinload(ContribuinteModel.danfes)
        )

        # filtros simples (Opção A): se campo existir no model, aplica igualdade.
        if filters:
            for col, val in filters.items():
                if hasattr(ContribuinteModel, col):
                    col_attr = getattr(ContribuinteModel, col)
                    # comportamento: se é string e param contém '%' -> LIKE; else if column name suggests nome -> LIKE %val%
                    if isinstance(val, str) and ("%" in val):
                        q = q.where(col_attr.like(val))
                    elif isinstance(val, str) and col.lower() in ("nm_fantasia", "nome", "descricao"):
                        q = q.where(col_attr.ilike(f"%{val}%"))
                    else:
                        q = q.where(col_attr == val)

        # ordenação segura (aplica apenas atributos existentes)
        if order:
            for field, direction in order:
                if hasattr(ContribuinteModel, field):
                    col_attr = getattr(ContribuinteModel, field)
                    if direction == "asc":
                        q = q.order_by(col_attr.asc())
                    else:
                        q = q.order_by(col_attr.desc())

        # paginação
        q = q.offset(offset).limit(limit)

        res = await self.session.execute(q)
        rows = res.scalars().all()

        out: List[Dict[str, Any]] = []
        for r in rows:
            item = {
                "cd_contribuinte": r.cd_contribuinte,
                "nm_fantasia": r.nm_fantasia,
                "cnpj_contribuinte": r.cnpj_contribuinte,
                "enderecos": [
                    {
                        "id_endereco": e.id_endereco,
                        "logradouro": e.logradouro,
                        "municipio": e.municipio,
                        "uf": e.uf
                    } for e in (r.enderecos or [])
                ],
                "danfes": [
                    {
                        "id_danfe": d.id_danfe,
                        "numero": d.numero,
                        "valor_total": d.valor_total,
                        "data_emissao": d.data_emissao.isoformat() if d.data_emissao else None
                    } for d in (r.danfes or [])
                ]
            }
            out.append(item)

        return out

    async def get_by_cd(self, cd_contribuinte: str) -> Optional[Dict[str, Any]]:
        q = select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
        res = await self.session.execute(q)
        obj = res.scalars().first()
        if not obj:
            return None
        return {
            "cd_contribuinte": obj.cd_contribuinte,
            "nm_fantasia": obj.nm_fantasia,
            "cnpj_contribuinte": obj.cnpj_contribuinte,
            "enderecos": [
                {"id_endereco": e.id_endereco, "logradouro": e.logradouro, "municipio": e.municipio, "uf": e.uf}
                for e in (obj.enderecos or [])
            ],
            "danfes": [
                {"id_danfe": d.id_danfe, "numero": d.numero, "valor_total": d.valor_total,
                 "data_emissao": d.data_emissao.isoformat() if d.data_emissao else None}
                for d in (obj.danfes or [])
            ]
        }

    async def get_by_cnpj(self, cnpj: str) -> Optional[Dict[str, Any]]:
        q = select(ContribuinteModel).where(ContribuinteModel.cnpj_contribuinte == cnpj)
        res = await self.session.execute(q)
        obj = res.scalars().first()
        if not obj:
            return None
        return {
            "cd_contribuinte": obj.cd_contribuinte,
            "nm_fantasia": obj.nm_fantasia,
            "cnpj_contribuinte": obj.cnpj_contribuinte,
            "enderecos": [],
            "danfes": []
        }

    async def create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        obj = ContribuinteModel(**payload)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return {
            "cd_contribuinte": obj.cd_contribuinte,
            "nm_fantasia": obj.nm_fantasia,
            "cnpj_contribuinte": obj.cnpj_contribuinte
        }

    async def update(self, cd_contribuinte: str, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        q = select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
        res = await self.session.execute(q)
        obj = res.scalars().first()
        if not obj:
            return None
        for k, v in payload.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        await self.session.flush()
        await self.session.refresh(obj)
        return {
            "cd_contribuinte": obj.cd_contribuinte,
            "nm_fantasia": obj.nm_fantasia,
            "cnpj_contribuinte": obj.cnpj_contribuinte
        }

    async def delete(self, cd_contribuinte: str) -> Optional[Dict[str, Any]]:
        q = select(ContribuinteModel).where(ContribuinteModel.cd_contribuinte == cd_contribuinte)
        res = await self.session.execute(q)
        obj = res.scalars().first()
        if not obj:
            return None
        await self.session.delete(obj)
        return {"cd_contribuinte": cd_contribuinte}
