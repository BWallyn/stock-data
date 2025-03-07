"""
This is a boilerplate pipeline 'download_data'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline

from stock_data.pipelines.download_data.nodes import download_data_range


def create_pipeline(**kwargs) -> Pipeline:
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
                name="Download_data_range",
            ),
        ],
        namespace="download_data",
        inputs=None,
        outputs="stock_data_aapl",
    )
