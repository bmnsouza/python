import time
import json
from sqlalchemy import event
from sqlalchemy.engine import Engine
from app.logger import sql_logger

# Limite em milissegundos para considerar uma query lenta
SLOW_QUERY_THRESHOLD_MS = 200


def setup_sql_audit(engine: Engine):
    """
    Adiciona eventos de auditoria SQL ao SQLAlchemy Engine.
    Gera logs estruturados com métricas de execução e alerta de lentidão.
    Compatível com SQLAlchemy Async (usa engine.sync_engine).
    """

    def safe_convert(value):
        """Garante que qualquer objeto seja serializável em JSON."""
        if value is None:
            return None
        if isinstance(value, (str, int, float, bool)):
            return value
        if isinstance(value, (list, tuple)):
            return [safe_convert(v) for v in value]
        if isinstance(value, dict):
            return {k: safe_convert(v) for k, v in value.items()}

        # Tenta converter objetos Oracle ou SQLAlchemy customizados
        try:
            return str(value)
        except Exception:
            return f"<non-serializable: {type(value).__name__}>"

    def sanitize_parameters(parameters):
        """Aplica safe_convert de forma recursiva."""
        try:
            if isinstance(parameters, (list, tuple)):
                return [safe_convert(p) for p in parameters]
            elif isinstance(parameters, dict):
                return {k: safe_convert(v) for k, v in parameters.items()}
            else:
                return safe_convert(parameters)
        except Exception:
            return "<unserializable parameters>"

    @event.listens_for(engine.sync_engine, "before_cursor_execute")
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        """Dispara antes de uma query ser executada."""
        conn.info.setdefault("query_start_time", []).append(time.perf_counter())

        log_entry = {
            "event": "sql_start",
            "statement": statement.strip(),
            "parameters": sanitize_parameters(parameters),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }

        sql_logger.debug(json.dumps(log_entry, ensure_ascii=False))

    @event.listens_for(engine.sync_engine, "after_cursor_execute")
    def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        """Dispara após a execução de uma query."""
        start_time = conn.info["query_start_time"].pop(-1)
        total_time = (time.perf_counter() - start_time) * 1000

        log_entry = {
            "event": "sql_complete",
            "statement": statement.strip(),
            "parameters": sanitize_parameters(parameters),
            "duration_ms": round(total_time, 2),
            "slow": total_time > SLOW_QUERY_THRESHOLD_MS,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }

        if total_time > SLOW_QUERY_THRESHOLD_MS:
            sql_logger.warning(json.dumps(log_entry, ensure_ascii=False))
        else:
            sql_logger.info(json.dumps(log_entry, ensure_ascii=False))
