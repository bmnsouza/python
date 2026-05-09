from dataclasses import dataclass
from typing import Any

import orjson


@dataclass(slots=True)
class BenchmarkResult:
    payload_size: float
    returned_rows: int


def measure_payload(payload: Any) -> float:
    """Calcula o tamanho real do payload serializado."""

    return round(len(orjson.dumps(payload)) / 1024, 2)


def count_rows(payload: Any) -> int:
    """Conta dinamicamente os registros retornados."""

    try:
        data = payload.get("data", {})

        if data:
            resolver_key = next(iter(data.keys()))
            resolver_data = data[resolver_key]

            if isinstance(resolver_data, dict):
                edges = resolver_data.get("edges", [])

                return sum(len(edge.get("node", {}).get("danfe", [])) for edge in edges)

        if isinstance(payload, list):
            return len(payload)

        return 1 if payload else 0

    except (AttributeError, KeyError, TypeError):
        return 0


def measure_all(payload: Any) -> BenchmarkResult:
    return BenchmarkResult(
        payload_size=measure_payload(payload),
        returned_rows=count_rows(payload),
    )
