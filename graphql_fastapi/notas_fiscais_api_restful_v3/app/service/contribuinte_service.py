from typing import Tuple, Dict, Any, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.contribuinte_repository import ContribuinteRepository
from app.utils.error_utils import map_data_base_error
from app.utils.format_contribuinte import format_contribuinte


class ContribuinteService:
    def __init__(self, session: AsyncSession):
        self.repo = ContribuinteRepository(session)

    # ---------------------------------------------------------------------
    async def list_contribuintes(
        self,
        filters: Dict[str, Any],
        order: List,
        offset: int,
        limit: int,
    ) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            total = await self.repo.count(filters)
            rows = await self.repo.list(filters, order, offset, limit)

            return total, [format_contribuinte(r) for r in rows]

        except Exception as e:
            map_data_base_error(e)

    # ---------------------------------------------------------------------
    async def get_contribuinte_por_cd(self, cd: str):
        try:
            r = await self.repo.get_by_cd(cd)
            if not r:
                return None

            return format_contribuinte(r)

        except Exception as e:
            map_data_base_error(e)

    # ---------------------------------------------------------------------
    async def get_contribuinte_por_cnpj(self, cnpj: str):
        try:
            r = await self.repo.get_by_cnpj(cnpj)
            if not r:
                return None

            return format_contribuinte(r)

        except Exception as e:
            map_data_base_error(e)

    # ---------------------------------------------------------------------
    async def create_contribuinte(self, payload: Dict[str, Any]):
        try:
            r = await self.repo.create(payload)
            return format_contribuinte(r)
        except Exception as e:
            map_data_base_error(e)

    # ---------------------------------------------------------------------
    async def update_contribuinte(self, cd: str, payload: Dict[str, Any]):
        try:
            r = await self.repo.update(cd, payload)
            if not r:
                return None

            return format_contribuinte(r)
        except Exception as e:
            map_data_base_error(e)

    # ---------------------------------------------------------------------
    async def delete_contribuinte(self, cd: str):
        try:
            r = await self.repo.delete(cd)
            if not r:
                return None
            return {"deleted": True}
        except Exception as e:
            map_data_base_error(e)
