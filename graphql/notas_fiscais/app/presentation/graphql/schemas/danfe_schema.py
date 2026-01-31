from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, field_validator, model_validator


class DanfeSchema(BaseModel):
    cd_contribuinte: Optional[str] = Field(default=None, min_length=9, max_length=20)
    numero: Optional[str] = Field(default=None, min_length=5, max_length=15)
    valor_total: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=2)
    data_emissao: Optional[date] = Field(default=None)

    @field_validator("data_emissao")
    @classmethod
    def validate_data_emissao_not_future(cls, value: Optional[date]):
        if value is not None and value < date(1900, 1, 1):
            raise ValueError("Data de emissão deve ser maior ou igual a 1900-01-01")

        if value is not None and value > date.today():
            raise ValueError("Data de emissão não pode ser futura")

        return value


class DanfeLastSevenDaysSchema(BaseModel):
    cd_contribuinte: str = Field(..., min_length=9, max_length=20)


class DanfeMonthlySchema(BaseModel):
    cd_contribuinte: str = Field(..., min_length=9, max_length=20)
    year: int = Field(..., ge=1900)
    month: int = Field(..., ge=1, le=12)

    @model_validator(mode="after")
    def validate_year_month_not_future(self):
        today = date.today()

        if (self.year, self.month) > (today.year, today.month):
            raise ValueError("O ano e o mês informados não podem ser posteriores ao mês atual")

        return self
