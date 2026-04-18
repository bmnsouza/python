from typing import Any

from sqlalchemy import text

from app.presentation.filters.contribuinte_filter import ContribuinteFilter, ContribuintesFilter

from ..builders.helpers.sql_helper import SqlHelper


class ContribuinteBuilder:

    class Contribuinte:

        _QUERY = """
        SELECT c.cnpj_contribuinte, c.nm_fantasia
        FROM nota_fiscal.contribuinte c
        WHERE c.cnpj_contribuinte = :cnpj
        """

        @classmethod
        def build_statement(cls, filtro: ContribuinteFilter) -> tuple[str, dict[str, Any]]:
            statement = text(cls._QUERY)
            parameters = filtro.parameters()

            return statement, parameters

    class Contribuintes:

        _QUERY = """
        SELECT c.cnpj_contribuinte, c.nm_fantasia
        FROM nota_fiscal.contribuinte c
        WHERE c.nm_fantasia LIKE '%' || :nmFantasia || '%'
        """

        @classmethod
        def build_statement(
            cls,
            filtro: ContribuintesFilter,
            offset: int,
            limit: int,
        ) -> tuple[str, dict[str, Any]]:
            query = cls._QUERY
            order_by = "nm_fantasia"

            statement = SqlHelper.paginate(query=query, order_by=order_by)
            parameters = filtro.parameters(offset=offset, limit=limit)

            return statement, parameters
