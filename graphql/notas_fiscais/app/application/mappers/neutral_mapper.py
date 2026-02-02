from typing import Any, Mapping


def to_neutral_dict(obj: Any) -> dict[str, Any] | None:

    if obj is None:
        return None

    # Já é dict
    if isinstance(obj, Mapping):
        return {k: v for k, v in obj.items() if v is not None}

    # Pydantic v2
    if hasattr(obj, "model_dump"):
        return {
            k: v
            for k, v in obj.model_dump().items()
            if v is not None
        }

    # Dataclass
    if hasattr(obj, "__dataclass_fields__"):
        return {
            k: getattr(obj, k)
            for k in obj.__dataclass_fields__
            if getattr(obj, k) is not None
        }

    # Objetos simples (GraphQL inputs entram aqui)
    if hasattr(obj, "__dict__"):
        return {
            k: v
            for k, v in vars(obj).items()
            if v is not None
        }

    raise TypeError(f"Tipo não suportado para conversão neutra: {type(obj)}")
