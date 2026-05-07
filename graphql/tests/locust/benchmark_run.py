import argparse
import shutil
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def run_locust(users, spawn_rate, run_time, csv_dir):
    """Executa o Locust em modo headless e salva CSVs na pasta correta."""
    subprocess.run(
        [
            "locust",
            "-f",
            "tests/locust/locustfile.py",
            "--host",
            "http://localhost:8080",
            "--users",
            str(users),
            "--spawn-rate",
            str(spawn_rate),
            "--csv",
            str((csv_dir / "locust").resolve()),
            "--headless",
            "--run-time",
            run_time,
        ],
        check=True,
    )


def generate_graphs(stats, png_dir):
    """Gera gráficos de latência, throughput e percentil 95."""
    stats.plot(x="Name", y="Average Response Time", kind="bar", legend=False)
    plt.ylabel("Tempo médio (ms)")
    plt.title("Latência média por endpoint")
    plt.tight_layout()
    plt.savefig(png_dir / "latencia_media.png")

    stats.plot(x="Name", y="Requests/s", kind="bar", legend=False, color="orange")
    plt.ylabel("Requisições por segundo")
    plt.title("Throughput por endpoint")
    plt.tight_layout()
    plt.savefig(png_dir / "throughput.png")

    stats.plot(x="Name", y="95%", kind="bar", legend=False, color="green")
    plt.ylabel("95º Percentil (ms)")
    plt.title("Tempo de resposta - 95º Percentil")
    plt.tight_layout()
    plt.savefig(png_dir / "percentil_95.png")


def write_report(stats, benchmark_csv, base_dir, png_dir):
    """Cria o relatório locust.md com tabela, gráficos, percentis e métricas extras."""
    total_requests = stats["Request Count"].sum()
    total_failures = stats["Failure Count"].sum()
    avg_latency = stats["Average Response Time"].mean()
    avg_throughput = stats["Requests/s"].mean()

    with open(base_dir / "locust.md", "w", encoding="utf-8") as f:
        f.write("# Relatório de Performance - Locust\n\n")
        f.write("## 📊 Estatísticas por endpoint\n")
        f.write(stats.to_markdown(index=False))
        f.write("\n\n## 📈 Gráficos\n")
        f.write("![Latência média](png/latencia_media.png)\n")
        f.write("![Throughput](png/throughput.png)\n")
        f.write("![Percentil 95](png/percentil_95.png)\n\n")
        f.write("## 📝 Interpretação\n")
        f.write(f"- Total de requisições: {total_requests}\n")
        f.write(f"- Falhas: {total_failures}\n")
        f.write(f"- Latência média geral: {avg_latency:.2f} ms\n")
        f.write(f"- Throughput médio: {avg_throughput:.2f} req/s\n")

        # Interpretação automática dos percentis
        if "95%" in stats.columns:
            for _, row in stats.iterrows():
                endpoint = row["Name"]
                p95 = row["95%"]
                f.write(f"- No endpoint **{endpoint}**, 95% das requisições responderam abaixo de {p95:.0f} ms\n")

        # Integra métricas de payload/memória
        if benchmark_csv.exists():
            f.write("\n\n## 📦 Métricas de Payload/Memória\n")
            bench = pd.read_csv(benchmark_csv)
            f.write(bench.to_markdown(index=False))


def main():
    parser = argparse.ArgumentParser(description="Executa benchmark com Locust e gera relatórios.")
    parser.add_argument("--users", type=int, default=100)
    parser.add_argument("--spawn-rate", type=int, default=10)
    parser.add_argument("--run-time", type=str, default="1m")
    args = parser.parse_args()

    base_dir = Path("tests/locust/reports")
    csv_dir = base_dir / "csv"
    png_dir = base_dir / "png"
    benchmark_csv = csv_dir / "locust_benchmark.csv"

    if base_dir.exists():
        shutil.rmtree(base_dir)

    csv_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)

    print("▶ Rodando Locust...")
    run_locust(args.users, args.spawn_rate, args.run_time, csv_dir)

    print("▶ Lendo CSV...")
    stats = pd.read_csv(csv_dir / "locust_stats.csv")

    print("▶ Gerando gráficos...")
    generate_graphs(stats, png_dir)

    print("▶ Atualizando relatório locust.md...")
    write_report(stats, benchmark_csv, base_dir, png_dir)

    print("✅ Benchmark finalizado! Relatórios disponíveis em tests/locust/reports")


if __name__ == "__main__":
    main()
