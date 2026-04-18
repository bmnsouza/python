from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class NodeWithRN(BaseModel, Generic[T]):
    dto: T
    rn: int


class PaginatedResult(BaseModel, Generic[T]):
    items: list[T]
