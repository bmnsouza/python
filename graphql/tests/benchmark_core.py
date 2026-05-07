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
    """Mede apenas o tempo de execução da função."""
    start = perf_counter()
    result = func(*args, **kwargs)
    total_time = round(perf_counter() - start, 6)
    return result, total_time

def measure_memory(func, *args, **kwargs):
    """Mede apenas o consumo de memória da função."""
    tracemalloc.start()
    result = func(*args, **kwargs)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_peak = round(peak / 1024 / 1024, 3)  # MB
    return memory_peak

def measure_payload(obj):
    """Calcula o tamanho do objeto em KB."""
    return round(sys.getsizeof(obj) / 1024, 3)

def _count_rows(result) -> int:
    """Conta dinamicamente o número de linhas retornadas pelo resolver."""
    try:
        data = result.get("data", {})
        if data:
            resolver_key = next(iter(data.keys()))  # pega o nome do resolver dinamicamente
            edges = data[resolver_key].get("edges", [])
            return sum(len(edge["node"].get("danfe", [])) for edge in edges)
        # fallback: lista simples
        return len(result) if isinstance(result, list) else (1 if result else 0)
    except Exception:
        return 0

def measure_all(func, *args, **kwargs) -> BenchmarkResult:
    """Executa a função e mede tempo, memória, payload e linhas retornadas."""
    # mede tempo
    result, total_time = measure_time(func, *args, **kwargs)
    # mede memória (executa a função de novo para capturar o pico)
    memory_peak = measure_memory(func, *args, **kwargs)

    payload_size = measure_payload(result)
    returned_rows = _count_rows(result)

    print(">>> result:", result)
    print(">>> returned_rows:", returned_rows)

    return BenchmarkResult(
        result=result,
        total_time=total_time,
        memory_peak=memory_peak,
        payload_size=payload_size,
        returned_rows=returned_rows,
    )
