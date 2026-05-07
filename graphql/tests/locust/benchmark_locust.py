# tests/locust/benchmark_locust.py

import csv
from dataclasses import asdict, dataclass
from datetime import datetime

from tests.benchmark_core import BenchmarkResult, measure_all


@dataclass
class BenchmarkRow:
    executed_at: str
    resolver: str
    total_time: float
    memory_peak: float
    payload_size: float
    returned_rows: int


CSV_FILE = "tests/locust/reports/locust_benchmark.csv"


def benchmark_request(resolver_name: str, payload, csv_file: str = CSV_FILE) -> BenchmarkRow:
    """
    Executa o cálculo de métricas usando benchmark_core e grava em CSV.
    Retorna um BenchmarkRow.
    """
    metrics: BenchmarkResult = measure_all(lambda: payload)

    row = BenchmarkRow(
        executed_at=datetime.now().isoformat(),
        resolver=resolver_name,
        total_time=metrics.total_time,
        memory_peak=metrics.memory_peak,
        payload_size=metrics.payload_size,
        returned_rows=metrics.returned_rows,
    )

    # Usa asdict para converter dataclass em dict
    row_dict = asdict(row)

    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row_dict.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(row_dict)

    return row
