# app/core/errors.py
from typing import Any, Dict, List, Optional
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel


class ErrorItem(BaseModel):
    code: str
    title: str
    description: str
    metadata: Optional[Dict[str, Any]] = None


class ErrorResponse(BaseModel):
    errors: List[ErrorItem]


def make_error(code: str, title: str, description: str, metadata: Optional[Dict[str, Any]] = None) -> ErrorResponse:
    return ErrorResponse(errors=[ErrorItem(code=code, title=title, description=description, metadata=metadata)])


# Registráveis em main.py:
async def http_exception_handler(request: Request, exc):
    status = getattr(exc, "status_code", 500)
    detail = getattr(exc, "detail", None)
    if isinstance(detail, dict) and "errors" in detail:
        body = detail
    else:
        body = make_error(code=str(status), title="HTTP Error", description=str(detail or exc)).dict()
    return JSONResponse(status_code=status, content=body)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = make_error(code="validation_error", title="Validation Error", description=str(exc)).dict()
    return JSONResponse(status_code=400, content=body)
