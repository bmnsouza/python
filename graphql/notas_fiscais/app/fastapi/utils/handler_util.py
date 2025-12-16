from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.fastapi.utils.exception_util import make_error


async def http_exception_handler(_request: Request, exc: HTTPException):
    """
    Somente o status 412 deve ser convertido para o formato de erro padrão.
    Qualquer outro HTTPException deve retornar exatamente como veio.
    """

    # Se NÃO for 412 → deixa o erro passar sem alterar
    if exc.status_code != 412:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )

    # A partir daqui, garantimos que é 412.
    # Agora aplicamos o formato padrão.

    # CASO 1 — Já está no formato do seu padrão
    if isinstance(exc.detail, dict) and "errors" in exc.detail:
        return JSONResponse(
            status_code=412,
            content=exc.detail
        )

    # CASO 2 — detail é uma lista
    if isinstance(exc.detail, list):
        body = make_error(
            code="412",
            title="HTTP 412 Error",
            description="Erro de pré-condição",
            metadata={"errors": exc.detail},
        ).model_dump()

        return JSONResponse(
            status_code=412,
            content=body
        )

    # CASO 3 — detail é string
    if isinstance(exc.detail, str):
        body = make_error(
            code="412",
            title="HTTP 412 Error",
            description=exc.detail,
        ).model_dump()

        return JSONResponse(
            status_code=412,
            content=body
        )

    # CASO 4 — fallback absoluto
    body = make_error(
        code="412",
        title="HTTP 412 Error",
        description=str(exc.detail),
    ).model_dump()

    return JSONResponse(
        status_code=412,
        content=body
    )


async def validation_exception_handler(_request: Request, exc: RequestValidationError):

    # Converte erros do Pydantic para o seu formato
    formatted_errors = []
    for err in exc.errors():
        formatted_errors.append({
            "loc": err.get("loc"),
            "msg": err.get("msg"),
            "type": err.get("type"),
            "input": err.get("input"),
            "ctx": err.get("ctx")
        })

    # ---- Usando seu objeto padrão ----
    body = make_error(
        code="VALIDATION_ERROR",
        title="Erro de validação",
        description="Um ou mais campos estão inválidos.",
        metadata={"errors": formatted_errors}
    ).model_dump()

    return JSONResponse(
        status_code=422,
        content=body
    )
