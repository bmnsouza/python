from functools import wraps

from app.core.benchmark import BenchmarkSession
from app.core import config


settings = config.get_settings()


def benchmark(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not settings.enable_benchmark:
            return await func(*args, **kwargs)

        session = BenchmarkSession(func.__module__ + "." + func.__name__)
        session.start()

        result = await func(*args, **kwargs)

        if isinstance(result, list):
            returned_rows = len(result)
        else:
            returned_rows = 1 if result is not None else 0

        await session.finish(returned_rows)

        return result

    return wrapper
