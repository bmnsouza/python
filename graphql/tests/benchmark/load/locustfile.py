import importlib.util
from pathlib import Path

from tests.benchmark.load.base_user import BaseGraphQLUser

SCENARIOS_DIR = Path(__file__).parent / "scenarios"


for scenario_file in SCENARIOS_DIR.glob("*.py"):
    module_name = scenario_file.stem

    spec = importlib.util.spec_from_file_location(
        module_name,
        scenario_file,
    )

    if not spec or not spec.loader:
        continue

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    for attr_name in dir(module):
        attr = getattr(module, attr_name)

        if isinstance(attr, type) and issubclass(attr, BaseGraphQLUser) and attr is not BaseGraphQLUser:
            globals()[attr_name] = attr
