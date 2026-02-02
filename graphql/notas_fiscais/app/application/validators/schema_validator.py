from typing import Any, Type, TypeVar
from pydantic import BaseModel

SchemaT = TypeVar("SchemaT", bound=BaseModel)


def validate_schema(
    *,
    data: Any | None,
    schema: Type[SchemaT],
) -> None:
    if data is None:
        return

    if isinstance(data, BaseModel):
        return

    if isinstance(data, dict):
        schema.model_validate(data)
        return

    schema.model_validate(vars(data))
