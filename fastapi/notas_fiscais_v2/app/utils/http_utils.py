from fastapi import HTTPException
from app.utils.error_utils import DuplicateEntryError, ForeignKeyError, DatabaseConnectionError
# from app.utils.format_utils import format_exception


def to_http_exception(exc: Exception) -> HTTPException:
    # raise HTTPException(
    #     status_code=404,
    #     detail={"errors": [{"code": "not_found", "title": "Not Found", "description": "Contribuinte não encontrado"}]},
    # )

    if isinstance(exc, DuplicateEntryError):
        return HTTPException(status_code=409, detail=str(exc))

    if isinstance(exc, ForeignKeyError):
        return HTTPException(status_code=400, detail=str(exc))

    if isinstance(exc, DatabaseConnectionError):
        return HTTPException(status_code=503, detail=str(exc))

    # raise HTTPException(status_code=500, detail=format_exception(str(e)))
    return HTTPException(status_code=500, detail="Erro interno inesperado")
