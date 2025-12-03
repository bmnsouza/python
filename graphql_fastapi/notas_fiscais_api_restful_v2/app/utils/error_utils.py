# app/utils/error_utils.py
from sqlalchemy.exc import IntegrityError, OperationalError


class DuplicateEntryError(Exception):
    pass


class ForeignKeyError(Exception):
    pass


class DatabaseConnectionError(Exception):
    pass


def map_data_base_error(e: Exception):
    """
    Padroniza exceções SQL para exceções da aplicação.
    Aqui você expande suas regras específicas para Oracle (ORA-xxxx).
    """
    msg = str(e)

    # ORACLE ERRORS -----------------------------------------------------
    if "ORA-00001" in msg:
        raise DuplicateEntryError("Registro já existe (ORA-00001)") from e

    if "ORA-02292" in msg:
        raise ForeignKeyError("Registro possui vínculos (ORA-02292)") from e

    if "ORA-12514" in msg or "ORA-12154" in msg:
        raise DatabaseConnectionError("Erro de conexão com Oracle") from e

    # SQLAlchemy generic ------------------------------------------------
    if isinstance(e, IntegrityError):
        raise DuplicateEntryError("Violação de integridade") from e

    if isinstance(e, OperationalError):
        raise DatabaseConnectionError("Erro operacional no banco") from e

    # fallback -----------------------------------------------------------
    raise e
