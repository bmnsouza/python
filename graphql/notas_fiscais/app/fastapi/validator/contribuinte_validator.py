from pydantic import BaseModel, Field

class ContribuintePath(BaseModel):
    cd_contribuinte: str = Field(..., min_length=9, max_length=20)
