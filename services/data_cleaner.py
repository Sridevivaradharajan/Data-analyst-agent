import pandas as pd
import numpy as np

def clean_data(df):
    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates()
    removed_duplicates = original_rows - len(df)

    # Replace missing values
    missing_before = df.isnull().sum().to_dict()
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna("Unknown", inplace=True)
    missing_after = df.isnull().sum().to_dict()

    return {
        "rows_before": original_rows,
        "rows_after": len(df),
        "duplicates_removed": removed_duplicates,
        "missing_before": missing_before,
        "missing_after": missing_after,
        "cleaned_preview": df.head(5).to_dict(orient="records")
    }
