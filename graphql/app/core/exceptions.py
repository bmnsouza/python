from typing import Any


class CustomException(Exception):
    """
    Exceção base customizada
    """

    def __init__(
        self,
        detail: str,
        status_code: int = 500,
        error_code: str = "INTERNAL_ERROR",
        data: dict[str, Any] | None = None,
    ):
        self.detail = detail
        self.status_code = status_code
        self.error_code = error_code
        self.data = data or {}
        super().__init__(self.detail)


class ValidationException(CustomException):
    """
    Exceção para erros de validação
    """

    def __init__(self, detail: str, data: dict[str, Any] | None = None):
        super().__init__(
            detail=detail,
            status_code=422,
            error_code="VALIDATION_ERROR",
            data=data,
        )
