import pandas as pd
import numpy as np

def analyze_data(df):
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    # Correlations
    correlations = numeric_df.corr().fillna(0).round(3).to_dict()

    # Summary statistics
    stats = {}
    for col in numeric_df.columns:
        stats[col] = {
            "mean": float(numeric_df[col].mean()),
            "median": float(numeric_df[col].median()),
            "min": float(numeric_df[col].min()),
            "max": float(numeric_df[col].max()),
            "std": float(numeric_df[col].std())
        }

    # Percentiles
    percentiles = numeric_df.quantile([0.25, 0.5, 0.75]).to_dict()

    return {
        "columns": list(df.columns),
        "correlations": correlations,
        "summary_statistics": stats,
        "percentiles": percentiles,
        "preview": df.head(5).to_dict(orient="records")
    }
