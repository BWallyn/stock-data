"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro 0.19.11"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from stock_data.pipelines.feature_engineering.nodes import (
    add_test_indicator,
    add_validation_indicator,
)


def create_pipeline(**kwargs) -> Pipeline:
    """Pipeline for feature engineering."""
    return pipeline(
        pipe=[
            node(
                func=add_test_indicator,
                inputs=["stock_data", "params:n_days"],
                outputs="df_w_test_indicator",
                name="Add_test_indicator",
            ),
            node(
                func=add_validation_indicator,
                inputs=["df_w_test_indicator", "params:n_days"],
                outputs="df_feat_engineered",
                name="Add_validation_indicator",
            ),
        ],
        inputs="stock_data",
        outputs="df_feat_engineered",
        namespace="feature_engineering",
    )
