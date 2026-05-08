import argparse
import shutil
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path("tests/benchmark/load/reports")
CSV_DIR = BASE_DIR / "csv"
PNG_DIR = BASE_DIR / "png"


class BenchmarkRunner:
    def __init__(self, users: int, spawn_rate: int, run_time: str):
        self.users = users
        self.spawn_rate = spawn_rate
        self.run_time = run_time

    def run(self):
        self._prepare_directories()
        self._execute_locust()

        stats = self._load_stats()

        self._generate_graphs(stats)
        self._generate_markdown(stats)

        print("✅ Benchmark finalizado!")
        print(f"📁 Relatórios disponíveis em: {BASE_DIR.resolve()}")

    def _prepare_directories(self):
        if BASE_DIR.exists():
            shutil.rmtree(BASE_DIR)

        CSV_DIR.mkdir(parents=True, exist_ok=True)
        PNG_DIR.mkdir(parents=True, exist_ok=True)

    def _execute_locust(self):
        print("▶ Executando Locust...")

        subprocess.run(
            [
                "locust",
                "-f",
                "tests/benchmark/load/load_test.py",
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

    def _load_stats(self) -> pd.DataFrame:
        print("▶ Carregando estatísticas...")

        stats = pd.read_csv(CSV_DIR / "load_stats.csv")

        return stats[
            ~stats["Name"].isin(
                [
                    "Aggregated",
                ]
            )
        ]

    def _generate_graphs(self, stats: pd.DataFrame):
        print("▶ Gerando gráficos...")

        self._generate_latency_graph(stats)
        self._generate_throughput_graph(stats)
        self._generate_p95_graph(stats)
        self._generate_payload_graph()

    def _generate_latency_graph(self, stats: pd.DataFrame):
        stats.plot(
            x="Name",
            y="Average Response Time",
            kind="bar",
            legend=False,
        )

        plt.ylabel("Tempo médio (ms)")
        plt.title("Latência média por endpoint")
        plt.tight_layout()
        plt.savefig(PNG_DIR / "latencia_media.png")
        plt.close()

    def _generate_throughput_graph(self, stats: pd.DataFrame):
        stats.plot(
            x="Name",
            y="Requests/s",
            kind="bar",
            legend=False,
        )

        plt.ylabel("Requisições por segundo")
        plt.title("Throughput por endpoint")
        plt.tight_layout()
        plt.savefig(PNG_DIR / "throughput.png")
        plt.close()

    def _generate_p95_graph(self, stats: pd.DataFrame):
        stats.plot(
            x="Name",
            y="95%",
            kind="bar",
            legend=False,
        )

        plt.ylabel("95º Percentil (ms)")
        plt.title("Percentil 95")
        plt.tight_layout()
        plt.savefig(PNG_DIR / "percentil_95.png")
        plt.close()

    def _generate_payload_graph(self):
        benchmark_csv = CSV_DIR / "load_benchmark.csv"

        if not benchmark_csv.exists():
            return

        benchmark = pd.read_csv(benchmark_csv)

        summary = benchmark.groupby("resolver").agg(payload_size_kb=("payload_size_kb", "mean")).reset_index()

        summary.plot(
            x="resolver",
            y="payload_size_kb",
            kind="bar",
            legend=False,
        )

        plt.ylabel("Payload médio (KB)")
        plt.title("Payload médio por endpoint")
        plt.tight_layout()
        plt.savefig(PNG_DIR / "payload_size.png")
        plt.close()

    def _generate_markdown(self, stats: pd.DataFrame):
        print("▶ Gerando relatório markdown...")

        benchmark_csv = CSV_DIR / "load_benchmark.csv"

        with open(BASE_DIR / "load.md", "w", encoding="utf-8") as file:
            file.write("# Relatório de Benchmark End-to-End\n\n")

            file.write("## Estatísticas do Locust\n\n")
            file.write(stats.to_markdown(index=False))

            file.write("\n\n## Gráficos\n\n")
            file.write("![Latência média](png/latencia_media.png)\n")
            file.write("![Throughput](png/throughput.png)\n")
            file.write("![Percentil 95](png/percentil_95.png)\n")
            file.write("![Payload médio](png/payload_size.png)\n")

            if benchmark_csv.exists():
                benchmark = pd.read_csv(benchmark_csv)

                summary = (
                    benchmark.groupby("resolver")
                    .agg(
                        payload_medio_kb=("payload_size_kb", "mean"),
                        registros_medios=("returned_rows", "mean"),
                    )
                    .reset_index()
                )

                file.write("\n\n## Payload e Registros\n\n")
                file.write(summary.to_markdown(index=False))


def parse_args():
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
