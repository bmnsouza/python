import sys
import tracemalloc
from dataclasses import dataclass
from time import perf_counter


@dataclass
class BenchmarkResult:
    result: object
    total_time: float
    memory_peak: float
    payload_size: float
    returned_rows: int


def measure_time(func, *args, **kwargs):
    start = perf_counter()
    result = func(*args, **kwargs)
    total_time = round(perf_counter() - start, 6)
    return result, total_time


def measure_memory(func, *args, **kwargs):
    tracemalloc.start()
    start = perf_counter()
    result = func(*args, **kwargs)
    total_time = round(perf_counter() - start, 6)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_peak = round(peak / 1024 / 1024, 3)  # MB
    return result, total_time, memory_peak


def measure_payload(obj):
    return round(sys.getsizeof(obj) / 1024, 3)  # KB


def measure_all(func, *args, **kwargs) -> BenchmarkResult:
    result, total_time, memory_peak = measure_memory(func, *args, **kwargs)
    payload_size = measure_payload(result)
    returned_rows = len(result) if isinstance(result, list) else (1 if result else 0)

    return BenchmarkResult(
        result=result,
        total_time=total_time,
        memory_peak=memory_peak,
        payload_size=payload_size,
        returned_rows=returned_rows,
    )
