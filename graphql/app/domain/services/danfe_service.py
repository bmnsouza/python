import logging
from collections.abc import Iterable

from app.domain.repositories.danfe_repository import DanfeRepository
from app.presentation.dtos.danfe_dto import DanfeDTO, DanfeItemDTO
from app.presentation.filters.danfe_filter import DanfesFilter

logger = logging.getLogger(__name__)


class DanfeService:

    def __init__(self, session):
        self.repo: DanfeRepository = DanfeRepository(session=session)

    async def get_danfes(self, *, filtro: DanfesFilter, offset: int, limit: int) -> list[DanfeDTO]:
        rows = await self.repo.get_danfes(filtro=filtro, offset=offset, limit=limit)
        return self._agrupar_danfes(rows)

    def _agrupar_danfes(self, rows: Iterable[dict]) -> list[DanfeDTO]:
        agrupados: dict[tuple, DanfeDTO] = {}

        for row in rows:
            chave = (
                row["cnpj_contribuinte"],
                row["nm_fantasia"],
                row["logradouro"],
                row["municipio"],
                row["uf"],
            )

            if chave not in agrupados:
                agrupados[chave] = DanfeDTO(
                    cnpj_contribuinte=row["cnpj_contribuinte"],
                    nm_fantasia=row["nm_fantasia"],
                    logradouro=row["logradouro"],
                    municipio=row["municipio"],
                    uf=row["uf"],
                    danfe=[],
                )

            agrupados[chave].danfe.append(
                DanfeItemDTO(
                    numero=row["numero"],
                    valor_total=row["valor_total"],
                    data_emissao=row["data_emissao"],
                )
            )

        return list(agrupados.values())
