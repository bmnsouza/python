from pydantic import BaseModel, Field


class EnderecoPath(BaseModel):
    id_endereco: int = Field(..., max_digits=10)
