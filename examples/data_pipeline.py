"""
Module: Data Pipeline Baseline
Version: 1.1.0
Author: Research Team
"""
from typing import Tuple
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_dataset(filepath: str) -> Tuple[pd.DataFrame, StandardScaler]:
    """Loads raw dataset from CSV, handles missing values, and normalizes numeric features."""
    df = pd.read_csv(filepath)
    df_clean = df.dropna().copy()
    
    scaler = StandardScaler()
    numeric_cols = df_clean.select_dtypes(include=["float64", "int64"]).columns
    df_clean[numeric_cols] = scaler.fit_transform(df_clean[numeric_cols])
    
    return df_clean, scaler
