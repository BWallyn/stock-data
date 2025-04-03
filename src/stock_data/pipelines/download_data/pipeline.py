"""This is a boilerplate pipeline 'download_data' generated using Kedro 0.19.11"""

from kedro.pipeline import Pipeline, node, pipeline

from stock_data.pipelines.download_data.nodes import download_data_range


def create_pipeline(**kwargs) -> Pipeline:
    """Pipeline to download data for a given stock name and date range."""
    return pipeline(
        pipe=[
            node(
                func=download_data_range,
                inputs=[
                    "params:stock_name_aapl",
                    "params:start_date",
                    "params:end_date",
                ],
                outputs="stock_data_aapl",
                name="Download_data_Apple",
            ),
            node(
                func=download_data_range,
                inputs=[
                    "params:stock_name_msft",
                    "params:start_date",
                    "params:end_date",
                ],
                outputs="stock_data_msft",
                name="Download_data_Microsoft",
            ),
            node(
                func=download_data_range,
                inputs=[
                    "params:stock_name_googl",
                    "params:start_date",
                    "params:end_date",
                ],
                outputs="stock_data_googl",
                name="Download_data_Google"
            ),
            node(
                func=download_data_range,
                inputs=[
                    "params:stock_name_amzn",
                    "params:start_date",
                    "params:end_date",
                ],
                outputs="stock_data_amzn",
                name="Download_data_Amazon"
            ),
            node(
                func=download_data_range,
                inputs=[
                    "params:stock_name_blk",
                    "params:start_date",
                    "params:end_date",
                ],
                outputs="stock_data_blk",
                name="Download_data_BlackRock"
            ),
        ],
        namespace="download_data",
        inputs=None,
        outputs=[
            "stock_data_aapl",
            "stock_data_msft",
            "stock_data_googl",
            "stock_data_amzn",
            "stock_data_blk",
        ],
    )
