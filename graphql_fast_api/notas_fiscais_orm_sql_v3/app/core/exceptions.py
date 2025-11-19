from oracledb import IntegrityError, DatabaseError as OracleDBError


class AppError(Exception):
    """Erro base da aplicação."""


class DuplicateEntryError(AppError):
    """Registro duplicado (ORA-00001)."""


class NotFoundError(AppError):
    """Registro não encontrado."""


class DatabaseError(AppError):
    """Erro genérico do banco."""


def map_data_base_error(e: Exception):
    """Mapeia erros Oracle para exceções da aplicação."""
    msg = str(e)

    # Viola restrição unique/pk
    if "ORA-00001" in msg:
        raise DuplicateEntryError("Registro já existe") from e

    # Erro genérico do OracleDB
    if isinstance(e, (OracleDBError, IntegrityError)):
        raise DatabaseError(f"Erro de banco de dados: {msg}") from e

    # Erro inesperado — deixa estourar
    raise e
