from typing import Any

from sqlalchemy import text

from app.domain.builders.helpers.sql_helper import SqlHelper
from app.presentation.filters.danfe_filter import DanfeFilter, DanfesFilter


class DanfeBuilder:

    class Danfe:

        _QUERY = """
        SELECT c.cnpj_contribuinte,
            c.nm_fantasia,
            d.numero,
            d.valor_total,
            d.data_emissao,
            e.logradouro,
            e.municipio,
            e.uf
        FROM nota_fiscal.contribuinte c
        INNER JOIN nota_fiscal.danfe d ON d.cnpj_contribuinte = c.cnpj_contribuinte
        INNER JOIN nota_fiscal.endereco e ON e.cnpj_contribuinte = c.cnpj_contribuinte
        WHERE d.numero = :numero
        """

        @classmethod
        def build_statement(cls, filtro: DanfeFilter) -> tuple[str, dict[str, Any]]:
            statement = text(cls._QUERY)
            parameters = filtro.parameters()

            return statement, parameters

    class Danfes:

        _QUERY = """
        SELECT c.cnpj_contribuinte,
            c.nm_fantasia,
            d.numero,
            d.valor_total,
            d.data_emissao,
            e.logradouro,
            e.municipio,
            e.uf
        FROM nota_fiscal.contribuinte c
        INNER JOIN nota_fiscal.danfe d ON d.cnpj_contribuinte = c.cnpj_contribuinte
        INNER JOIN nota_fiscal.endereco e ON e.cnpj_contribuinte = c.cnpj_contribuinte
        WHERE c.cnpj_contribuinte = :cnpj
            AND EXTRACT (YEAR FROM d.data_emissao) = :ano
        """

        @classmethod
        def build_statement(
            cls,
            filtro: DanfesFilter,
            offset: int,
            limit: int,
        ) -> tuple[str, dict[str, Any]]:
            query = cls._QUERY
            order_by = "nm_fantasia, data_emissao"

            statement = SqlHelper.paginate(query=query, order_by=order_by)
            parameters = filtro.parameters(offset=offset, limit=limit)

            return statement, parameters
