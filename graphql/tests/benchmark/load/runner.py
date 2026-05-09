import argparse
import shutil
import subprocess
from pathlib import Path

from tests.benchmark.load.reporting import charts, data_loader, report_builder

BASE_DIR = Path("tests/benchmark/load/output")
CSV_DIR = BASE_DIR / "csv"
IMAGES_DIR = BASE_DIR / "images"


class BenchmarkRunner:
    def __init__(self, users: int, spawn_rate: int, run_time: str):
        self.users = users
        self.spawn_rate = spawn_rate
        self.run_time = run_time

    def run(self) -> None:
        self._prepare_directories()
        self._execute_locust()

        print("▶ Carregando dados...")
        data = data_loader.load(CSV_DIR)

        print("▶ Gerando gráficos...")
        charts.generate_all(data, IMAGES_DIR)

        print("▶ Gerando dashboard HTML...")
        report_builder.generate(data, BASE_DIR, self.users, self.spawn_rate, self.run_time)

        print("✅ Benchmark finalizado!")
        print(f"📁 Relatório disponível em: {BASE_DIR.resolve()}")

    def _prepare_directories(self) -> None:
        if BASE_DIR.exists():
            shutil.rmtree(BASE_DIR)
        CSV_DIR.mkdir(parents=True, exist_ok=True)
        IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    def _execute_locust(self) -> None:
        print("▶ Executando Locust...")
        subprocess.run(
            [
                "locust",
                "-f",
                "tests/benchmark/load/locustfile.py",
                "--host",
                "http://localhost:8080",
                "--users",
                str(self.users),
                "--spawn-rate",
                str(self.spawn_rate),
                "--headless",
                "--run-time",
                self.run_time,
                "--csv",
                str((CSV_DIR / "load").resolve()),
            ],
            check=False,
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Executa benchmark end-to-end com Locust.")
    parser.add_argument("--users", type=int, default=100)
    parser.add_argument("--spawn-rate", type=int, default=10)
    parser.add_argument("--run-time", type=str, default="1m")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    BenchmarkRunner(
        users=args.users,
        spawn_rate=args.spawn_rate,
        run_time=args.run_time,
    ).run()
