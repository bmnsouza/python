from typing import Any

from sqlalchemy import text

from app.presentation.filters.endereco_filter import EnderecoFilter, EnderecosFilter

from ..builders.helpers.sql_helper import SqlHelper


class EnderecoBuilder:

    class Endereco:

        _QUERY = """
        SELECT e.cnpj_contribuinte, e.logradouro, e.municipio, e.uf
        FROM nota_fiscal.endereco e
        WHERE e.cnpj_contribuinte = :cnpj
        """

        @classmethod
        def build_statement(cls, filtro: EnderecoFilter) -> tuple[str, dict[str, Any]]:
            statement = text(cls._QUERY)
            parameters = filtro.parameters()

            return statement, parameters

    class Enderecos:

        _QUERY = """
        SELECT e.cnpj_contribuinte, e.logradouro, e.municipio, e.uf
        FROM nota_fiscal.endereco e
        WHERE e.uf = :uf
          AND e.municipio = :municipio
        """

        @classmethod
        def build_statement(
            cls,
            filtro: EnderecosFilter,
            offset: int,
            limit: int,
        ) -> tuple[str, dict[str, Any]]:
            query = cls._QUERY
            order_by = "uf, municipio, logradouro"

            statement = SqlHelper.paginate(query=query, order_by=order_by)
            parameters = filtro.parameters(offset=offset, limit=limit)

            return statement, parameters
