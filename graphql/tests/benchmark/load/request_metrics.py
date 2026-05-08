import csv
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

from locust import events

from tests.benchmark.core import BenchmarkResult, measure_all


@dataclass(slots=True)
class BenchmarkRow:
    executed_at: str
    resolver: str
    payload_size_kb: float
    returned_rows: int


CSV_FILE = Path("tests/benchmark/load/reports/csv/load_benchmark.csv")

BENCHMARK_ROWS: list[BenchmarkRow] = []


def collect_request_metrics(
    resolver_name: str,
    payload,
) -> BenchmarkRow:
    metrics: BenchmarkResult = measure_all(payload)

    row = BenchmarkRow(
        executed_at=datetime.now().isoformat(),
        resolver=resolver_name,
        payload_size_kb=metrics.payload_size_kb,
        returned_rows=metrics.returned_rows,
    )

    BENCHMARK_ROWS.append(row)

    return row


@events.quitting.add_listener
def save_metrics(environment, **kwargs):
    if not BENCHMARK_ROWS:
        return

    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=asdict(BENCHMARK_ROWS[0]).keys(),
        )

        writer.writeheader()

        for row in BENCHMARK_ROWS:
            writer.writerow(asdict(row))
