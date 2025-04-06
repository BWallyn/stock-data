"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro 0.19.11"""

# =================
# ==== IMPORTS ====
# =================

import pandas as pd

# ===================
# ==== FUNCTIONS ====
# ===================

def add_test_indicator(df: pd.DataFrame, n_days: str) -> pd.DataFrame:
    """Add a test indicator column to the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        n_days (int): Number of days to use for the test indicator.

    Returns:
        (pd.DataFrame): DataFrame with the test indicator column added.

    """
    df["test"] = df["date"].between(
        df["date"].max() - pd.Timedelta(days=n_days),
        df["date"].max()
    )
    return df


def add_validation_indicator(df: pd.DataFrame, n_days: int) -> pd.DataFrame:
    """Add a validation indicator column to the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        n_days (int): Number of days to use for the validation indicator.

    Returns:
        (pd.DataFrame): DataFrame with the validation indicator column added.

    """
    df["validation"] = df["date"].between(
        df[df["test"] == 0]["date"].max() - pd.Timedelta(days=n_days),
        df[df["test"] == 0]["date"].max()
    )
    return df
