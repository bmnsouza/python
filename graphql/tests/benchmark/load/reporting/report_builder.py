from pathlib import Path

import pandas as pd

from tests.benchmark.load.reporting.data_loader import BenchmarkData

COLORS = ["#378ADD", "#D85A30", "#1D9E75", "#D4537E", "#BA7517"]


def generate(data: BenchmarkData, base_dir: Path, users: int, spawn_rate: int, run_time: str) -> None:
    ctx = _build_context(data, users, spawn_rate, run_time)
    html = _render(ctx)
    (base_dir / "report.html").write_text(html, encoding="utf-8")


def _build_context(data: BenchmarkData, users: int, spawn_rate: int, run_time: str) -> dict:
    stats = data.stats
    total_failures = int(stats["Failure Count"].sum())

    return {
        "users": users,
        "spawn_rate": spawn_rate,
        "run_time": run_time,
        "total_requests": int(stats["Request Count"].sum()),
        "total_failures": total_failures,
        "total_rps": round(stats["Requests/s"].sum(), 2),
        "min_latency": round(stats["Min Response Time"].min()),
        "failure_color": "#16a34a" if total_failures == 0 else "#dc2626",
        "failure_icon": "✅" if total_failures == 0 else "❌",
        "kpi_requests_rows": _kpi_ep_rows(stats, "Request Count", int),
        "kpi_rps_rows": _kpi_ep_rows(stats, "Requests/s", lambda v: f"{v:.2f} req/s"),
        "kpi_failures_rows": _kpi_ep_rows(stats, "Failure Count", int),
        "kpi_latency_rows": _kpi_ep_rows(stats, "Min Response Time", lambda v: f"{round(v):,} ms"),
        "stats_rows_html": _stats_rows(stats),
        "perc_html": _percentile_rows(stats),
        "failures_section": _failures_section(data.failures),
        "payload_section": _payload_section(data.benchmark),
        "history_section": _history_section(data.history),
        "chart_labels_js": str(list(stats["Name"])),
        "chart_bg_js": str([COLORS[i % len(COLORS)] for i in range(len(stats))]),
        "avg_latency": list(stats["Average Response Time"].round().astype(int)),
        "throughput": list(stats["Requests/s"].round(2)),
        "p95": list(stats["95%"].astype(int)),
        "payload_data_js": _payload_chart_data(data.benchmark, stats),
    }


def _payload_chart_data(benchmark: pd.DataFrame | None, stats: pd.DataFrame) -> str:
    if benchmark is not None and "payload_size" in benchmark.columns:
        summary = benchmark.groupby("resolver")["payload_size"].mean()
        data = [float(round(summary.get(name, 0), 2)) for name in stats["Name"]]
        return str(data)
    return str([round(v / 1024, 2) for v in stats["Average Content Size"].tolist()])


def _kpi_ep_rows(stats: pd.DataFrame, col: str, fmt) -> str:
    return "\n".join(
        f"<li style='color:{COLORS[i % len(COLORS)]}'>"
        f"<span class='kpi-ep-name'>{row['Name']}</span>"
        f"<span class='kpi-ep-val'>{fmt(row[col])}</span>"
        f"</li>"
        for i, (_, row) in enumerate(stats.iterrows())
    )


def _stats_rows(stats: pd.DataFrame) -> str:
    rows = []
    for i, (_, row) in enumerate(stats.iterrows()):
        color = COLORS[i % len(COLORS)]
        bg = _rgba(color, 0.12)
        fc = "#16a34a" if row["Failure Count"] == 0 else "#dc2626"
        rows.append(
            f"<tr>"
            f"<td><span class='pill' style='background:{bg};color:{color}'>{row['Name']}</span></td>"
            f"<td>{int(row['Request Count'])}</td>"
            f"<td style='color:{fc}'>{int(row['Failure Count'])}</td>"
            f"<td>{int(row['Median Response Time']):,}</td>"
            f"<td>{round(row['Average Response Time']):,}</td>"
            f"<td>{round(row['Min Response Time']):,}</td>"
            f"<td>{round(row['Max Response Time']):,}</td>"
            f"<td>{round(row['Requests/s'], 2)}</td>"
            f"<td>{int(row['Average Content Size']):,} B</td>"
            f"</tr>"
        )
    return "\n".join(rows)


def _percentile_rows(stats: pd.DataFrame) -> str:
    perc_cols = ["50%", "66%", "75%", "80%", "90%", "95%", "98%", "99%", "99.9%", "99.99%", "100%"]
    rows = []
    names = list(stats["Name"])

    for _, row in stats.iterrows():
        color = COLORS[names.index(row["Name"]) % len(COLORS)]
        bg = _rgba(color, 0.12)
        cells = "".join(f"<td>{int(row[p]):,}</td>" for p in perc_cols if p in row)
        rows.append(
            f"<tr><td><span class='pill' style='background:{bg};color:{color}'>{row['Name']}</span></td>"
            f"{cells}</tr>"
        )
    return "\n".join(rows)


def _failures_section(failures: pd.DataFrame) -> str:
    if failures.empty:
        return ""

    rows = "".join(
        f"<tr><td>{row.get('Method', '-')}</td>"
        f"<td>{row.get('Name', '-')}</td>"
        f"<td style='color:#f87171;font-family:monospace;font-size:11px'>{row.get('Error', '-')}</td>"
        f"<td>{int(row.get('Occurrences', 0))}</td></tr>"
        for _, row in failures.iterrows()
    )

    return f"""
    <section>
      <p class="section-label">🚨 Falhas detectadas</p>
      <div class="card">
        <div class="scroll">
          <table>
            <thead>
              <tr>
                <th>Método</th>
                <th>Endpoint</th>
                <th>Erro</th>
                <th>Ocorrências</th>
              </tr>
            </thead>
            <tbody>
              {rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
    """


def _payload_section(benchmark: pd.DataFrame | None) -> str:
    if benchmark is None:
        return ""

    summary = (
        benchmark.groupby("resolver")
        .agg(payload_medio=("payload_size", "mean"), registros_medios=("returned_rows", "mean"))
        .reset_index()
    )

    rows = "".join(
        f"<tr><td>{row['resolver']}</td><td>{float(row['payload_medio']):.2f} KB</td>"
        f"<td>{int(row['registros_medios'])}</td></tr>"
        for _, row in summary.iterrows()
    )

    return f"""
    <section>
      <p class="section-label">📦 Payload e Registros</p>
      <div class="card">
        <div class="scroll">
          <table>
            <thead>
              <tr>
                <th>Resolver</th>
                <th>Payload médio</th>
                <th>Registros médios</th>
              </tr>
            </thead>
            <tbody>
              {rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
    """


def _history_section(history: pd.DataFrame | None) -> str:
    """Gráficos de evolução temporal usando dados Aggregated do load_stats_history.csv."""
    if history is None or history.empty:
        return ""

    agg = (
        history.groupby("elapsed_s")
        .agg(avg_lat=("Total Average Response Time", "mean"), rps=("Requests/s", "mean"), users=("User Count", "max"))
        .reset_index()
    )

    timestamps = agg["elapsed_s"].tolist()
    lat_vals = [round(float(v)) for v in agg["avg_lat"]]
    rps_vals = [round(float(v), 2) for v in agg["rps"]]
    user_vals = [int(v) for v in agg["users"]]

    return f"""
    <section>
      <p class="section-label">📉 Evolução temporal</p>
      <div class="charts-grid">
        <div class="chart-card">
          <h3>Latência média ao longo do tempo (ms)</h3>
          <div style="position:relative;height:200px">
            <canvas id="cHistLat"></canvas>
          </div>
        </div>
        <div class="chart-card">
          <h3>Throughput e usuários ao longo do tempo</h3>
          <div style="position:relative;height:200px">
            <canvas id="cHistRps"></canvas>
          </div>
        </div>
      </div>
    </section>
    <script>
      (function() {{
        const histTs = {timestamps};
        const lineCfg = (datasets, yLabel, extraScales) => ({{
          type: 'line',
          data: {{ labels: histTs, datasets }},
          options: {{
            responsive: true, maintainAspectRatio: false,
            plugins: {{ legend: {{ labels: {{ color: '#8b90a8', font: {{ size: 10 }}, boxWidth: 10 }} }} }},
            scales: {{
              x: {{ grid: {{ color: 'rgba(255,255,255,.06)' }},
                    ticks: {{ color: '#8b90a8', font: {{ size: 9 }}, callback: (_, i) => histTs[i] + 's' }} }},
              y: {{ grid: {{ color: 'rgba(255,255,255,.06)' }}, ticks: {{ color: '#8b90a8', font: {{ size: 10 }} }},
                    title: {{ display: true, text: yLabel, color: '#545878', font: {{ size: 10 }} }} }},
              ...extraScales
            }}
          }}
        }});
        new Chart(document.getElementById('cHistLat'), lineCfg([
          {{label:'Latência média',data:{lat_vals},borderColor:'#378ADD',backgroundColor:'rgba(55,138,221,0.08)',
            fill:true,tension:0.3,pointRadius:2}}
        ], 'ms', {{}}));
        new Chart(document.getElementById('cHistRps'), lineCfg([
          {{label:'Req/s',data:{rps_vals},borderColor:'#1D9E75',backgroundColor:'rgba(29,158,117,0.08)',fill:true,
            tension:0.3,pointRadius:2}},
          {{label:'Usuários',data:{user_vals},borderColor:'#6366f1',backgroundColor:'rgba(99,102,241,0.08)',fill:true,
            tension:0.3,pointRadius:2,yAxisID:'yU'}}
        ], 'req/s', {{
          yU: {{ position: 'right', grid: {{ display: false }},
                ticks: {{ color: '#6366f1', font: {{ size: 10 }} }},
                title: {{ display: true, text: 'usuários', color: '#6366f1', font: {{ size: 10 }} }} }}
        }}));
      }})();
    </script>
    """


def _rgba(hex_color: str, alpha: float) -> str:
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    return f"rgba({r},{g},{b},{alpha})"


def _render(c: dict) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Benchmark End-to-End</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
        <style>
          *{{box-sizing:border-box;margin:0;padding:0}}
          :root{{--bg:#0f1117;--surface:#1a1d27;--border:#2e3347;--text:#e8eaf0;--muted:#8b90a8;--hint:#545878}}
          body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);
            color:var(--text);padding:32px 24px;min-height:100vh}}
          h1{{font-size:22px;font-weight:600;margin-bottom:4px}}
          .subtitle{{font-size:13px;color:var(--muted);margin-bottom:28px}}
          .badge{{display:inline-flex;align-items:center;gap:5px;font-size:11px;padding:3px 9px;border-radius:20px;
            background:rgba(74,222,128,.12);color:#4ade80;margin-left:10px;vertical-align:middle}}
          section{{margin-bottom:32px}}
          .section-label{{font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;
            color:var(--muted);margin-bottom:12px}}
          .kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px}}
          .kpi{{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 16px}}
          .kpi em{{font-size:11px;font-style:normal;color:var(--muted);display:block;margin-bottom:6px}}
          .kpi strong{{font-size:26px;font-weight:600;display:block}}
          .charts-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
          .chart-card{{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:16px}}
          .chart-card h3{{font-size:12px;font-weight:500;color:var(--muted);margin-bottom:12px}}
          table{{width:100%;border-collapse:collapse;font-size:12px}}
          th{{text-align:left;color:var(--hint);font-weight:500;padding:6px 10px 10px;
            border-bottom:1px solid var(--border);white-space:nowrap}}
          td{{padding:9px 10px;border-bottom:1px solid var(--border);color:var(--text);white-space:nowrap}}
          tr:last-child td{{border-bottom:none}}
          .pill{{padding:2px 9px;border-radius:20px;font-size:11px;font-weight:500}}
          .card{{background:var(--surface);border:1px solid var(--border);border-radius:10px;overflow:hidden}}
          .card .scroll{{overflow-x:auto}}
          footer{{font-size:11px;color:var(--hint);border-top:1px solid var(--border);padding-top:16px;
            display:flex;gap:20px;flex-wrap:wrap}}
          .kpi-ep-list{{list-style:none;margin-top:8px;display:flex;flex-direction:column;gap:4px;max-height:90px;
            overflow-y:auto;padding-right:4px}}
          .kpi-ep-list::-webkit-scrollbar{{width:3px}}.kpi-ep-list::-webkit-scrollbar-thumb{{background:var(--border);
            border-radius:2px}}
          .kpi-ep-list li{{display:flex;justify-content:space-between;align-items:center;font-size:11px;gap:8px}}
          .kpi-ep-name{{color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1}}
          .kpi-ep-val{{font-weight:600;white-space:nowrap;flex-shrink:0}}
          @media(max-width:600px){{.charts-grid{{grid-template-columns:1fr}}}}
        </style>
      </head>
      <body>
        <h1>
          📊 Relatório de Benchmark End-to-End
          <span class="badge">{c['failure_icon']} {c['total_failures']} falhas</span>
        </h1>
        <p class="subtitle">Locust headless · POST · host localhost:8080</p>
        <section>
          <p class="section-label">⚡ Visão geral</p>
          <div class="kpi-grid">
            <div class="kpi">
              <em>Total de requisições</em><strong>{c['total_requests']}</strong>
              <ul class="kpi-ep-list">{c['kpi_requests_rows']}</ul>
            </div>
            <div class="kpi">
              <em>Falhas</em><strong style="color:{c['failure_color']}">{c['total_failures']}</strong>
              <ul class="kpi-ep-list">{c['kpi_failures_rows']}</ul>
            </div>
            <div class="kpi">
              <em>Throughput total</em><strong>{c['total_rps']} req/s</strong>
              <ul class="kpi-ep-list">{c['kpi_rps_rows']}</ul>
            </div>
            <div class="kpi">
              <em>Menor latência</em><strong>{c['min_latency']:,} ms</strong>
              <ul class="kpi-ep-list">{c['kpi_latency_rows']}</ul>
            </div>
          </div>
        </section>
        <section>
          <p class="section-label">📈 Gráficos de desempenho</p>
          <div class="charts-grid">
            <div class="chart-card">
              <h3>Latência média (ms)</h3>
              <div style="position:relative;height:180px">
                <canvas id="cLat"></canvas>
              </div>
            </div>
            <div class="chart-card">
              <h3>Throughput (req/s)</h3>
              <div style="position:relative;height:180px">
                <canvas id="cRps"></canvas>
              </div>
            </div>
            <div class="chart-card">
              <h3>Percentil 95 (ms)</h3>
              <div style="position:relative;height:180px">
                <canvas id="cP95"></canvas>
              </div>
            </div>
            <div class="chart-card">
              <h3>Payload médio (KB)</h3>
              <div style="position:relative;height:180px">
                <canvas id="cPay"></canvas>
              </div>
            </div>
          </div>
        </section>
        <section>
          <p class="section-label">🔬 Estatísticas completas</p>
          <div class="card">
            <div class="scroll">
              <table>
                <thead>
                  <tr>
                    <th>Endpoint</th>
                    <th>Requisições</th>
                    <th>Falhas</th>
                    <th>Mediana (ms)</th>
                    <th>Média (ms)</th>
                    <th>Mín (ms)</th>
                    <th>Máx (ms)</th>
                    <th>Req/s</th>
                    <th>Tam. médio</th>
                  </tr>
                </thead>
                <tbody>{c['stats_rows_html']}</tbody>
              </table>
            </div>
          </div>
        </section>
        <section>
          <p class="section-label">📐 Distribuição de percentis (ms)</p>
          <div class="card">
            <div class="scroll">
              <table>
                <thead>
                  <tr>
                    <th>Endpoint</th>
                    <th>p50</th>
                    <th>p66</th>
                    <th>p75</th>
                    <th>p80</th>
                    <th>p90</th>
                    <th>p95</th>
                    <th>p98</th>
                    <th>p99</th>
                    <th>p99.9</th>
                    <th>p99.99</th>
                    <th>p100</th>
                  </tr>
                </thead>
                <tbody>{c['perc_html']}</tbody>
              </table>
            </div>
          </div>
        </section>
        {c['history_section']}
        {c['failures_section']}
        {c['payload_section']}
        <footer>
          <span>🖥 Gerado via Locust headless</span>
          <span>👥 Usuários: {c['users']} · Spawn rate: {c['spawn_rate']}/s · Tempo: {c['run_time']}</span>
        </footer>
        <script>
          const labels = {c['chart_labels_js']};
          const colors = {c['chart_bg_js']};
          const cfg = (data, yLabel) => ({{
            type: 'bar',
            data: {{ labels, datasets: [{{ data, backgroundColor: colors, borderRadius: 5, borderSkipped: false }}] }},
            options: {{
              responsive: true, maintainAspectRatio: false,
              plugins: {{ legend: {{ display: false }} }},
              scales: {{
                x: {{ grid: {{ display: false }}, ticks: {{ color: '#8b90a8', font: {{ size: 10 }} }} }},
                y: {{ grid: {{ color: 'rgba(255,255,255,.06)' }}, ticks: {{ color: '#8b90a8', font: {{ size: 10 }} }},
                    title: {{ display: true, text: yLabel, color: '#545878', font: {{ size: 10 }} }} }}
              }}
            }}
          }});
          new Chart(document.getElementById('cLat'), cfg({c['avg_latency']}, 'ms'));
          new Chart(document.getElementById('cRps'), cfg({c['throughput']}, 'req/s'));
          new Chart(document.getElementById('cP95'), cfg({c['p95']}, 'ms'));
          new Chart(document.getElementById('cPay'), cfg({c['payload_data_js']}, 'KB'));
        </script>
      </body>
    </html>
    """
