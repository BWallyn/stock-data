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
    feature_engineering_amzn_pipeline = feature_engineering.create_fe_amzn()
    feature_engineering_blk_pipeline = feature_engineering.create_fe_blk()
    feature_engineering_googl_pipeline = feature_engineering.create_fe_googl()
    feature_engineering_msft_pipeline = feature_engineering.create_fe_msft()
    # Register the pipelines
    return {
        "__default__": (
            download_data_pipeline
            + feature_engineering_aapl_pipeline
            + feature_engineering_amzn_pipeline
            + feature_engineering_blk_pipeline
            + feature_engineering_googl_pipeline
            + feature_engineering_msft_pipeline
        ),
        "download_data": download_data_pipeline,
        "feature_engineering_aapl": feature_engineering_aapl_pipeline,
        "feature_engineering_amzn": feature_engineering_amzn_pipeline,
        "feature_engineering_blk": feature_engineering_blk_pipeline,
        "feature_engineering_googl": feature_engineering_googl_pipeline,
        "feature_engineering_msft": feature_engineering_msft_pipeline,
    }
