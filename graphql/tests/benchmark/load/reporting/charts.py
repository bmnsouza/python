from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from tests.benchmark.load.reporting.data_loader import BenchmarkData


def generate_all(data: BenchmarkData, images_dir: Path) -> None:
    _latency(data.stats, images_dir)
    _throughput(data.stats, images_dir)
    _p95(data.stats, images_dir)
    _payload(data, images_dir)


def _latency(stats: pd.DataFrame, images_dir: Path) -> None:
    stats.plot(x="Name", y="Average Response Time", kind="bar", legend=False)
    plt.ylabel("Tempo médio (ms)")
    plt.title("Latência média por endpoint")
    plt.tight_layout()
    plt.savefig(images_dir / "latencia_media.png")
    plt.close()


def _throughput(stats: pd.DataFrame, images_dir: Path) -> None:
    stats.plot(x="Name", y="Requests/s", kind="bar", legend=False)
    plt.ylabel("Requisições por segundo")
    plt.title("Throughput por endpoint")
    plt.tight_layout()
    plt.savefig(images_dir / "throughput.png")
    plt.close()


def _p95(stats: pd.DataFrame, images_dir: Path) -> None:
    stats.plot(x="Name", y="95%", kind="bar", legend=False)
    plt.ylabel("95º Percentil (ms)")
    plt.title("Percentil 95")
    plt.tight_layout()
    plt.savefig(images_dir / "percentil_95.png")
    plt.close()


def _payload(data: BenchmarkData, images_dir: Path) -> None:
    if data.benchmark is None:
        return

    summary = data.benchmark.groupby("resolver").agg(payload_size=("payload_size", "mean")).reset_index()
    summary.plot(x="resolver", y="payload_size", kind="bar", legend=False)
    plt.ylabel("Payload médio (KB)")
    plt.title("Payload médio por endpoint")
    plt.tight_layout()
    plt.savefig(images_dir / "payload_size.png")
    plt.close()
