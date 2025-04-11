"""Project pipelines."""

from kedro.pipeline import Pipeline

from stock_data.pipelines import (
    download_data,
    feature_engineering,
)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.

    """
    # Define all available pipelines
    download_data_pipeline = download_data.create_pipeline()
    feature_engineering_aapl_pipeline = feature_engineering.create_fe_aapl()
    # Register the pipelines
    return {
        "__default__": (
            download_data_pipeline
            + feature_engineering_aapl_pipeline
        ),
        "download_data": download_data_pipeline,
        "feature_engineering_aapl": feature_engineering_aapl_pipeline,
    }
