from pathlib import Path

from .settings import REPORTS_DIR


def save_text(name: str, text: str, suffix: str = ".md") -> Path:
    REPORTS_DIR.mkdir(exist_ok=True)
    path = REPORTS_DIR / f"{name}{suffix}"
    path.write_text(text, encoding="utf-8")
    return path


def load_text(name: str, suffix: str = ".md") -> str:
    path = REPORTS_DIR / f"{name}{suffix}"
    if not path.is_file():
        raise FileNotFoundError(f"{path} not found. Run the step that creates it first.")
    return path.read_text(encoding="utf-8")