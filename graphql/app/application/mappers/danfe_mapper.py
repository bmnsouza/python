from collections.abc import Iterable

from app.application.dtos.danfe_dto import DanfeDTO, DanfeItemDTO


class DanfeMapper:

    @staticmethod
    def agrupar(rows: Iterable[dict]) -> list[DanfeDTO]:
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
