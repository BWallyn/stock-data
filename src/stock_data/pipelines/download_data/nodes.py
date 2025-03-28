"""This is a boilerplate pipeline 'download_data' generated using Kedro 0.19.11"""

# =================
# ==== IMPORTS ====
# =================

import pandas as pd
import yfinance as yf

# ===================
# ==== FUNCTIONS ====
# ===================


def download_data_range(
    stock_name: str, start_date: str, end_date: str
) -> pd.DataFrame:
    """Download stock data from Yahoo Finance for a given date range.

    Args:
        stock_name (str): Name of the stock.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        (pd.DataFrame): Stock data for the given date range.

    """
    # Download stock data from Yahoo Finance
    return yf.download(stock_name, start=start_date, end=end_date)


def download_data_day(stock_name: str) -> pd.DataFrame:
    """Download stock data from Yahoo Finance for the last day.

    Args:
        stock_name (str): Name of the stock.

    Returns:
        (pd.DataFrame): Stock data for the last day

    """
    return yf.download(stock_name, period="1d")
