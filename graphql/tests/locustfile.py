from pathlib import Path
import importlib.util

# from scenarios.danfe_locust import DanfesJsonPythonUser, DanfesJsonBancoUser


SCENARIOS_DIR = Path(__file__).parent / "scenarios"


for scenario_file in SCENARIOS_DIR.glob("*_locust.py"):
    module_name = scenario_file.stem

    spec = importlib.util.spec_from_file_location(module_name, scenario_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
