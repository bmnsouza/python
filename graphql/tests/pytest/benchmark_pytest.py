TOTAL_TIME = 5.0
MEMORY_PEAK = 8.0
PAYLOAD_SIZE = 500


def assert_benchmark(metrics):
    assert metrics.total_time < TOTAL_TIME, f"Tempo: {metrics.total_time}s"
    assert metrics.memory_peak < MEMORY_PEAK, f"Memória: {metrics.memory_peak}MB"
    assert metrics.payload_size < PAYLOAD_SIZE, f"Payload: {metrics.payload_size}KB"
