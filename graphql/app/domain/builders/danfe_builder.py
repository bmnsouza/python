from typing import Any

from sqlalchemy import text

from app.domain.builders.helpers.sql_helper import SqlHelper
from app.presentation.filters.danfe_filter import DanfesFilter


class DanfeBuilder:

    class Danfes:

        _QUERY = f"""
        SELECT c.cnpj_contribuinte,
                c.nm_fantasia,
                d.numero,
                d.valor_total,
                d.data_emissao,
                e.logradouro,
                e.municipio,
                e.uf
        FROM (
            SELECT c.cnpj_contribuinte,
                c.nm_fantasia
            FROM nota_fiscal.contribuinte c
            ORDER BY c.nm_fantasia
            {SqlHelper.pagination()}
        ) c
        INNER JOIN nota_fiscal.danfe d ON d.cnpj_contribuinte = c.cnpj_contribuinte
        INNER JOIN nota_fiscal.endereco e ON e.cnpj_contribuinte = c.cnpj_contribuinte
        WHERE EXTRACT (YEAR FROM d.data_emissao) = :ano
        ORDER BY c.nm_fantasia, d.data_emissao
        """

        @classmethod
        def build_statement(
            cls,
            filtro: DanfesFilter,
            offset: int,
            limit: int,
        ) -> tuple[str, dict[str, Any]]:

            statement = text(cls._QUERY)
            parameters = filtro.parameters(offset=offset, limit=limit)

            return statement, parameters
