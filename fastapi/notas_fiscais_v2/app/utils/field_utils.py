from typing import List, Optional


def parse_fields_param(fields: Optional[str]) -> Optional[List[str]]:
    if not fields:
        return None
    return [f.strip() for f in fields.split(",") if f.strip()]


def select_fields_from_obj(obj, fields: Optional[List[str]] = None):
    # Pydantic v2
    if hasattr(obj, "model_dump"):
        obj_dict = obj.model_dump()
    # SQLAlchemy
    elif hasattr(obj, "__table__"):
        obj_dict = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    # Já é dict
    else:
        obj_dict = obj

    if not fields:
        return obj_dict

    return {k: v for k, v in obj_dict.items() if k in fields}
