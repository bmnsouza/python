from typing import Any

from sqlalchemy import text

from app.domain.builders.helpers.sql_helper import SqlHelper
from app.presentation.filters.danfe_filter import DanfesFilter


class DanfeBuilder:

    class DanfesJsonPython:

        _QUERY = f"""
        WITH danfes_filtradas AS (
            SELECT d.cnpj_contribuinte,
                d.numero,
                d.valor_total,
                d.data_emissao
            FROM nota_fiscal.danfe d
            WHERE EXTRACT(YEAR FROM d.data_emissao) = :ano
        ),
        contribuintes_paginados AS (
            SELECT DISTINCT
                c.cnpj_contribuinte,
                c.nm_fantasia
            FROM nota_fiscal.contribuinte c
            INNER JOIN danfes_filtradas d ON d.cnpj_contribuinte = c.cnpj_contribuinte
            ORDER BY c.nm_fantasia
            {SqlHelper.pagination()}
        )
        SELECT c.cnpj_contribuinte,
            c.nm_fantasia,
            d.numero,
            d.valor_total,
            d.data_emissao,
            e.logradouro,
            e.municipio,
            e.uf
        FROM contribuintes_paginados c
        INNER JOIN danfes_filtradas d ON d.cnpj_contribuinte = c.cnpj_contribuinte
        INNER JOIN nota_fiscal.endereco e ON e.cnpj_contribuinte = c.cnpj_contribuinte
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

    class DanfesJsonBanco:

        _QUERY = f"""
        WITH contribuintes_paginados AS (
            SELECT
                c.cnpj_contribuinte,
                c.nm_fantasia
            FROM nota_fiscal.contribuinte c
            ORDER BY c.nm_fantasia
            {SqlHelper.pagination()}
        ),
        danfes_agrupados AS (
            SELECT
                d.cnpj_contribuinte,
                JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'numero' VALUE d.numero,
                        'valor_total' VALUE d.valor_total,
                        'data_emissao' VALUE d.data_emissao
                    )
                    ORDER BY d.data_emissao
                ) AS danfe
            FROM nota_fiscal.danfe d
            INNER JOIN contribuintes_paginados cp ON cp.cnpj_contribuinte = d.cnpj_contribuinte
            WHERE EXTRACT(YEAR FROM d.data_emissao) = :ano
            GROUP BY d.cnpj_contribuinte
        )
        SELECT
            cp.cnpj_contribuinte,
            cp.nm_fantasia,
            e.logradouro,
            e.municipio,
            e.uf,
            COALESCE(da.danfe, '[]') AS danfe
        FROM contribuintes_paginados cp
        INNER JOIN nota_fiscal.endereco e ON e.cnpj_contribuinte = cp.cnpj_contribuinte
        LEFT JOIN danfes_agrupados da ON da.cnpj_contribuinte = cp.cnpj_contribuinte
        ORDER BY cp.nm_fantasia
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
