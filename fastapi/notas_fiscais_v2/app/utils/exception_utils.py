from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from fastapi import HTTPException
from app.utils.error_utils import DuplicateEntryError, ForeignKeyError, DatabaseConnectionError


class ErrorItem(BaseModel):
    code: str
    title: str
    description: str
    metadata: Optional[Dict[str, Any]] = None


class ErrorResponse(BaseModel):
    errors: List[ErrorItem]


def make_error(code: str, title: str, description: str, metadata: Optional[Dict[str, Any]] = None) -> ErrorResponse:
    return ErrorResponse(errors=[
        ErrorItem(code=code, title=title, description=description, metadata=metadata)
    ])


def raise_http_exception(exc: Exception = None, *, status_code: int = None, code: str = None, title: str = None, description: str = None, metadata=None) -> HTTPException:
    # Exceção da aplicação
    if exc is not None:
        if isinstance(exc, ForeignKeyError):
            raise HTTPException(status_code=400, detail=str(exc))

        if isinstance(exc, DuplicateEntryError):
            raise HTTPException(status_code=409, detail=str(exc))

        if isinstance(exc, DatabaseConnectionError):
            raise HTTPException(status_code=503, detail=str(exc))

        raise HTTPException(status_code=500, detail="Erro interno inesperado")

    # lançamento customizado
    body = make_error(
        code=str(code or status_code),
        title=title or "HTTP Error",
        description=description or "",
        metadata=metadata,
    ).model_dump()

    raise HTTPException(status_code=status_code, detail=body)
