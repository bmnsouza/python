from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field

from app.domain.values.contribuinte_value import CdContribuinte
from app.domain.values.data_value import field_date_validator_not_future, year_month_validator_not_future
from app.presentation.graphql.inputs.order_input import OrderDirection


class DanfeListFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte | None = None
    numero: str | None = Field(default=None, min_length=5, max_length=15)
    valor_total: Decimal | None = Field(default=None, max_digits=12, decimal_places=2)
    data_emissao: date | None = Field(default=None)

    _validate_data_emissao = field_date_validator_not_future("data_emissao")


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

    _validate_year_month = year_month_validator_not_future("year", "month")
