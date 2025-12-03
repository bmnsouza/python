from typing import Any, Dict, Optional


def format_contribuinte(obj) -> Optional[Dict[str, Any]]:
    if obj is None:
        return None

    def fmt_endereco(e):
        return {
            "id_endereco": e.id_endereco,
            "logradouro": e.logradouro,
            "municipio": e.municipio,
            "uf": e.uf,
        }

    def fmt_danfe(d):
        return {
            "id_danfe": d.id_danfe,
            "numero": d.numero,
            "valor_total": d.valor_total,
            "data_emissao": d.data_emissao.isoformat() if d.data_emissao else None,
        }

    return {
        "cd_contribuinte": obj.cd_contribuinte,
        "nm_fantasia": obj.nm_fantasia,
        "cnpj_contribuinte": obj.cnpj_contribuinte,
        "enderecos": [fmt_endereco(e) for e in (obj.enderecos or [])],
        "danfes": [fmt_danfe(d) for d in (obj.danfes or [])],
    }
