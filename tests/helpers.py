import importlib.util
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISE_DIR = ROOT / os.environ.get("EXERCISE_DIR", "solutions")


def exercise_path(relative_path: str) -> Path:
    return EXERCISE_DIR / relative_path


def run_script(relative_path: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(exercise_path(relative_path))],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )


def import_exercise(relative_path: str):
    path = exercise_path(relative_path)
    if not path.exists():
        raise FileNotFoundError(f"exercise file not found: {path}")

    module_name = relative_path.removesuffix(".py").replace("/", "_").replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load exercise: {path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module
