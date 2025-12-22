from pydantic import BaseModel, Field


class DanfePath(BaseModel):
    id_danfe: int = Field(..., max_digits=10)
