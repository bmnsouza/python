from datetime import datetime, time
from decimal import Decimal, InvalidOperation

from typing import Any, Dict, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.logger import app_logger
from app.fastapi.schema.danfe_schema import Danfe
from app.repository.danfe_repository import DanfeRepository
from app.utils.error_util import map_data_base_error
from app.utils.exception_util import raise_http_exception


class DanfeService:
    def __init__(self, session: AsyncSession):
        self.repo = DanfeRepository(session)


    async def get_list(self, filters: Dict[str, Any], order: List, offset: int, limit: int) -> Tuple[int, List[Dict[str, Any]]]:
        try:
            # Valida e normaliza antes de chamar o repository
            filters = validate_and_normalize_filters(filters)

            total = await self.repo.count(filters)
            rows = await self.repo.get_list(filters, order, offset, limit)

            return total, [Danfe.model_validate(r) for r in rows]
        except Exception as e:
            app_logger.exception("Erro ao obter danfes %s", e)
            map_data_base_error(e)


    async def get_by_id(self, id: int):
        try:
            r = await self.repo.get_by_id(id)
            if not r:
                return None

            return Danfe.model_validate(r)
        except Exception as e:
            app_logger.exception("Erro ao obter danfe por id %s", e)
            map_data_base_error(e)


    async def create(self, payload: Dict[str, Any]):
        try:
            r = await self.repo.create(payload)
            return Danfe.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def update(self, id: int, payload: Dict[str, Any]):
        try:
            r = await self.repo.update(id, payload)
            if not r:
                return None

            return Danfe.model_validate(r)
        except Exception as e:
            map_data_base_error(e)


    async def delete(self, id: int):
        try:
            r = await self.repo.delete(id)
            if not r:
                return None
            return {"deleted": True}
        except Exception as e:
            map_data_base_error(e)


def validate_and_normalize_filters(filters: Dict[str, Any]) -> Dict[str, Any]:
    new_filters = filters.copy()

    # Valida o filtro valor_total
    if "valor_total" in new_filters and new_filters["valor_total"] is not None:
        raw = new_filters["valor_total"]
        try:
            valor = Decimal(str(raw))
        except InvalidOperation as e:
            raise_http_exception(exc=e, description="O campo 'valor_total' deve ser numérico.")

        new_filters["valor_total"] = valor

    # Valida o filtro data_emissao
    if "data_emissao" in new_filters and new_filters["data_emissao"]:
        raw = new_filters["data_emissao"]

        try:
            dt = datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError as e:
            raise_http_exception(exc=e, description="O campo 'data_emissao' deve estar no formato YYYY-MM-DD.")

        # Cria intervalo do dia
        start = datetime.combine(dt, time.min)
        end = datetime.combine(dt, time.max)

        new_filters["data_emissao_inicio"] = start
        new_filters["data_emissao_fim"] = end

        # Remove o campo original
        del new_filters["data_emissao"]

    return new_filters
