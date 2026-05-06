from __future__ import annotations

import asyncio
import csv
import os
import tracemalloc

from datetime import datetime
from time import perf_counter


_csv_lock = asyncio.Lock()


class BenchmarkSession:
    def __init__(self, resolver_name: str):
        self.resolver_name = resolver_name
        self.started_at = 0.0
        self.memory_start = 0

    def start(self):
        self.started_at = perf_counter()
        self.memory_start = tracemalloc.get_traced_memory()[1]

    async def finish(self, returned_rows: int):
        total_time = perf_counter() - self.started_at
        memory_end = tracemalloc.get_traced_memory()[1]
        memory_peak_mb = round((memory_end - self.memory_start) / 1024 / 1024, 3)

        row = {
            "executed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "resolver": self.resolver_name,
            "total_time": round(total_time, 6),
            "memory_peak_mb": memory_peak_mb,
            "returned_rows": returned_rows,
        }

        csv_file = f"tests/reports/benchmark_{self.resolver_name}.csv"

        async with _csv_lock:
            file_exists = os.path.isfile(csv_file)

            with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=row.keys())

                if not file_exists:
                    writer.writeheader()

                writer.writerow(row)

        print(row)
