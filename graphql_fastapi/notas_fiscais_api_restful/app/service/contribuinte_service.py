# app/service/contribuinte_service.py
from typing import Dict, List, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.contribuinte_repository import ContribuinteRepository


class ContribuinteService:
    def __init__(self, session: AsyncSession):
        self.repo = ContribuinteRepository(session)

    async def list_contribuintes(
        self,
        filters: Optional[Dict[str, str]] = None,
        order: Optional[List[Tuple[str, str]]] = None,
        offset: int = 0,
        limit: int = 50
    ) -> Tuple[int, List[Dict]]:
        total = await self.repo.count(filters)
        items = await self.repo.list(filters=filters, order=order, offset=offset, limit=limit)
        return total, items

    async def get_contribuinte_por_cd(self, cd_contribuinte: str) -> Optional[Dict]:
        return await self.repo.get_by_cd(cd_contribuinte)

    async def get_contribuinte_por_cnpj(self, cnpj: str) -> Optional[Dict]:
        return await self.repo.get_by_cnpj(cnpj)

    async def create_contribuinte(self, payload: Dict) -> Dict:
        return await self.repo.create(payload)

    async def update_contribuinte(self, cd_contribuinte: str, payload: Dict) -> Optional[Dict]:
        return await self.repo.update(cd_contribuinte, payload)

    async def delete_contribuinte(self, cd_contribuinte: str) -> Optional[Dict]:
        return await self.repo.delete(cd_contribuinte)
