"""
Module: Data Pipeline Baseline
Version: 1.0.0
Author: Research Team
"""
import pandas as pd


def load_dataset(filepath: str) -> pd.DataFrame:
    """Loads raw dataset from CSV."""
    df = pd.read_csv(filepath)
    return df.dropna()
