from decimal import InvalidOperation
from graphql import GraphQLError

from sqlalchemy.exc import IntegrityError, OperationalError


class DuplicateEntryError(Exception):
    pass


class ForeignKeyError(Exception):
    pass


class DatabaseConnectionError(Exception):
    pass


def map_data_base_error(e: Exception):
    msg = str(e)

    if "ORA-00001" in msg:
        raise DuplicateEntryError("Registro já existe (ORA-00001)") from e

    if "ORA-02292" in msg:
        raise ForeignKeyError("Registro possui vínculos (ORA-02292)") from e

    if "ORA-12514" in msg or "ORA-12154" in msg:
        raise DatabaseConnectionError("Erro de conexão com Oracle") from e

    if isinstance(e, IntegrityError):
        raise DuplicateEntryError("Violação de integridade") from e

    if isinstance(e, OperationalError):
        raise DatabaseConnectionError("Erro operacional no banco") from e

    raise e


def raise_graphql_error(exc: Exception = None, *, code: str = None, title: str = None, description: str = None) -> None:

    # Se já é GraphQLError → relança
    if isinstance(exc, GraphQLError):
        raise exc

    # Exceção de domínio
    if exc is not None:
        if isinstance(exc, (ForeignKeyError, InvalidOperation, ValueError)):
            raise GraphQLError(
                message="Erro de validação",
                extensions={
                    "code": "VALIDATION_ERROR",
                    "title": "Erro de validação",
                    "description": str(exc),
                },
            )

        if isinstance(exc, DuplicateEntryError):
            raise GraphQLError(
                message="Conflito",
                extensions={
                    "code": "CONFLICT",
                    "title": "Conflito de dados",
                    "description": str(exc),
                },
            )

        if isinstance(exc, DatabaseConnectionError):
            raise GraphQLError(
                message="Serviço indisponível",
                extensions={
                    "code": "SERVICE_UNAVAILABLE",
                    "title": "Erro de infraestrutura",
                    "description": str(exc),
                },
            )

        # fallback real
        raise GraphQLError(
            message="Erro interno",
            extensions={
                "code": "INTERNAL_SERVER_ERROR",
                "title": "Erro interno",
                "description": "Erro interno inesperado",
            },
        )

    # Erro manual (description)
    raise GraphQLError(
        message=title or "Erro de validação",
        extensions={
            "code": code or "VALIDATION_ERROR",
            "title": title or "Erro de validação",
            "description": description or ""
        },
    )
