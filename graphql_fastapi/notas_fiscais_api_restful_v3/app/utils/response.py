from pydantic import BaseModel
from typing import Any, Optional


class SingleResponse(BaseModel):
    message: str
    data: Optional[Any] = None
    meta: Optional[dict] = None
