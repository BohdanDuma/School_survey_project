from pathlib import Path
import pandas as pd


def extract_raw(path: str) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f'Raw file not found at{path}')
    df = pd.read_csv(path/'Методика скринінг  (Ответы) - Ответы на форму (1).csv')
    return df

