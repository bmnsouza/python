from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd


@dataclass
class BenchmarkData:
    stats: pd.DataFrame
    failures: pd.DataFrame
    benchmark: pd.DataFrame | None = field(default=None)


def load(csv_dir: Path) -> BenchmarkData:
    stats = _load_stats(csv_dir)
    failures = _load_failures(csv_dir)
    benchmark = _load_benchmark(csv_dir)
    return BenchmarkData(stats=stats, failures=failures, benchmark=benchmark)


def _load_stats(csv_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_dir / "load_stats.csv")
    return df[~df["Name"].isin(["Aggregated"])].reset_index(drop=True)


def _load_failures(csv_dir: Path) -> pd.DataFrame:
    path = csv_dir / "load_failures.csv"
    if not path.exists():
        return pd.DataFrame(columns=["Method", "Name", "Error", "Occurrences"])

    # O Locust no Windows grava com a codificação do sistema (cp1252).
    # Tenta UTF-8 primeiro; cai para latin-1 se falhar.
    for encoding in ("utf-8", "latin-1"):
        try:
            df = pd.read_csv(path, encoding=encoding)
            return df if not df.empty else pd.DataFrame(columns=["Method", "Name", "Error", "Occurrences"])
        except UnicodeDecodeError:
            continue

    # Último recurso: substitui bytes inválidos por '?'
    df = pd.read_csv(path, encoding="utf-8", encoding_errors="replace")
    return df if not df.empty else pd.DataFrame(columns=["Method", "Name", "Error", "Occurrences"])


def _load_benchmark(csv_dir: Path) -> pd.DataFrame | None:
    path = csv_dir / "load_benchmark.csv"
    return pd.read_csv(path) if path.exists() else None
