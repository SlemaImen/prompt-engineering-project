import json
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_credentials(config_file: str = "config.json") -> tuple[str, str | None]:
    """Variables d'environnement d'abord, config.json ensuite."""
    key = os.environ.get("OPENAI_API_KEY")
    base = os.environ.get("OPENAI_BASE_URL")
    if key:
        return key, base

    path = PROJECT_ROOT / config_file
    if not path.is_file():
        raise FileNotFoundError(f"{path} introuvable")
    config = json.loads(path.read_text(encoding="utf-8"))
    return config["API_KEY"], config.get("OPENAI_API_BASE")