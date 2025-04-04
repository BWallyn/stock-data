"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro 0.19.11"""

# =================
# ==== IMPORTS ====
# =================

import pandas as pd

# ===================
# ==== FUNCTIONS ====
# ===================

def add_test_indicator(df: pd.DataFrame, date_test: str) -> pd.DataFrame:
    """Add a test indicator column to the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        date_test (str): Date to use for the test indicator.

    Returns:
        (pd.DataFrame): DataFrame with the test indicator column added.

    """
    df["test"] = df["date"] >= date_test
    return df
