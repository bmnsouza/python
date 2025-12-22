from typing import Optional
from pydantic import BaseModel, Field


class ContribuinteFilterParams(BaseModel):
    cd_contribuinte: Optional[str] = Field(default=None, min_length=9, max_length=20)
    cnpj_contribuinte: Optional[str] = Field(default=None, min_length=14, max_length=14)
    nm_fantasia: Optional[str] = Field(default=None, min_length=5, max_length=200)
