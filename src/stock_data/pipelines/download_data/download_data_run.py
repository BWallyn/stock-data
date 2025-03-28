# =================
# ==== IMPORTS ====
# =================

import logging
import os

import pandas as pd

from stock_data.pipelines.download_data.nodes import download_data_day
from stock_data.utils.utils import generate_timestamp

# Options
logger = logging.getLogger(__name__)

# ===================
# ==== FUNCTIONS ====
# ===================


def save_data(df: pd.DataFrame, stock_name: str, path_data: str) -> None:
    """Save the dataset to a specific file with the timestamp used for versionning.

    Args:
        df (pd.DataFrame): DataFrame to save.
        stock_name (str): Name of the stock to save.
        path_data (str): Path to the data folder.

    Returns:
        None

    """
    timestamp = generate_timestamp()
    logger.info("Saving dataset...")
    df.to_parquet(os.path.join(path_data, f"stock_{stock_name}_{timestamp}.parquet"))
    logger.info("Dataset saved")


def main(stock_name: str, path_data: str) -> None:
    """Download the data for a given stock and save it.

    Args:
        stock_name (str): Name of the stock.
        path_data (str): Path to the data folder.

    Returns:
        None

    """
    df_stock = download_data_day(stock_name=stock_name)
    save_data(df_stock, stock_name, path_data)


# =============
# ==== RUN ====
# =============

if __name__ == "__main__":
    # Options
    stock_name: str = "AAPL"
    path_data: str = "data/01_raw"

    # Run
    main(stock_name=stock_name, path_data=path_data)
