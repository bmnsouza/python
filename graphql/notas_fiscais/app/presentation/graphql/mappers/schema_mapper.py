from typing import Any, Optional, Type, TypeVar
from pydantic import BaseModel

SchemaT = TypeVar("SchemaT", bound=BaseModel)


def map_to_schema(
    *,
    data: Any | None,
    schema: Type[SchemaT]
) -> Optional[SchemaT]:
    if data is None:
        return None

    if isinstance(data, BaseModel):
        return data

    if isinstance(data, dict):
        return schema.model_validate(data)

    return schema.model_validate(vars(data))
