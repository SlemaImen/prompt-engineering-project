from pathlib import Path

import pandas as pd

from .settings import CSV_FILE, SAMPLE_SIZE

def load_events(path: Path, sample_size: int = 25) -> pd.DataFrame:
    """Charge le CSV et garde les `sample_size` premiers événements."""
    df = pd.read_csv(path)
    return df.head(sample_size).reset_index(drop=True)


def build_business_context(df: pd.DataFrame) -> str:
    """Transforme chaque ligne du tableau en bloc de texte lisible par l'IA."""
    parts = []
    for position, (_, row) in enumerate(df.iterrows(), start=1):
        parts.append(f"\n========== Supply Chain Disruption Event {position} ==========\n")
        for column in df.columns:
            parts.append(f"{column.replace('_', ' ').title()}: {row[column]}\n")
        parts.append("\n")
    return "".join(parts)


def load_business_context() -> str:
    """Raccourci utilisé par toutes les étapes."""
    return build_business_context(load_events(CSV_FILE, SAMPLE_SIZE))