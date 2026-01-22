import json
import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import app_logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        start_time = time.perf_counter()

        # Log de início da requisição
        app_logger.info(json.dumps({
            "event": "http_request_start",
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }, ensure_ascii=False))

        try:
            response = await call_next(request)
        except Exception as e:
            duration_ms = (time.perf_counter() - start_time) * 1000
            app_logger.exception(json.dumps({
                "event": "http_request_error",
                "request_id": request_id,
                "error": str(e),
                "duration_ms": round(duration_ms, 2),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            }, ensure_ascii=False))
            raise

        duration_ms = (time.perf_counter() - start_time) * 1000

        # Log de finalização da requisição
        app_logger.info(json.dumps({
            "event": "http_request_end",
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": round(duration_ms, 2),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }, ensure_ascii=False))

        # Inclui headers de auditoria
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Response-Time-ms"] = f"{duration_ms:.2f}"
        return response
