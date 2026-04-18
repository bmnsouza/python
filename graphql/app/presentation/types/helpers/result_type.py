from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginatedResult(BaseModel, Generic[T]):
    items: list[T]
