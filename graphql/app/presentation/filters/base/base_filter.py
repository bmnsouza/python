from typing import Any

from pydantic import BaseModel, ConfigDict


class BaseFilter(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    def parameters(
        self,
        offset: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        parameters: dict[str, Any] = self.model_dump(exclude_none=True)

        if offset is not None:
            parameters["offset"] = offset
        if limit is not None:
            parameters["limit"] = limit

        return parameters
