from typing import Optional

import strawberry


@strawberry.input
class ContribuinteParamsInput:
    cd_contribuinte: Optional[str] = None
    cnpj_contribuinte: Optional[str] = None
    nm_fantasia: Optional[str] = None
