from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator, model_validator

from app.domain.values.contribuinte_value import CdContribuinte
from app.presentation.graphql.inputs.order_input import OrderDirection


class DanfeListFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte | None = None
    numero: str | None = Field(default=None, min_length=5, max_length=15)
    valor_total: Decimal | None = Field(default=None, max_digits=12, decimal_places=2)
    data_emissao: date | None = Field(default=None)

    @field_validator("data_emissao")
    @classmethod
    def validate_data_emissao_not_future(cls, value: date | None):
        if value is None:
            return value

        if value < date(1900, 1, 1):
            raise ValueError("Data de emissão deve ser ≥ 1900-01-01")

        if value > date.today():
            raise ValueError("Data de emissão não pode ser futura")

        return value


class DanfeListOrderInputValidator(BaseModel):
    cd_contribuinte: OrderDirection | None = Field(default=None)
    numero: OrderDirection | None = Field(default=None)
    valor_total: OrderDirection | None = Field(default=None)
    data_emissao: OrderDirection | None = Field(default=None)


class DanfeLastSevenDaysFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte


class DanfeMonthlyFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte
    year: int = Field(..., ge=1900)
    month: int = Field(..., ge=1, le=12)

    @model_validator(mode="after")
    def validate_year_month_not_future(self):
        today = date.today()

        if (self.year, self.month) > (today.year, today.month):
            raise ValueError("O ano e o mês informados não podem ser posteriores ao mês atual")

        return self
