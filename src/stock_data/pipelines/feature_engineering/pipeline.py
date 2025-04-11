"""This is a boilerplate pipeline 'feature_engineering' generated using Kedro 0.19.11"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from stock_data.pipelines.feature_engineering.nodes import (
    add_test_indicator,
    add_validation_indicator,
)


def feature_engineering_template(**kwargs) -> Pipeline:
    """Pipeline template for feature engineering."""
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
    )


def create_fe_aapl(**kwargs) -> Pipeline:
    """Create the pipeline for feature engineering."""
    return pipeline(
        pipe=feature_engineering_template(**kwargs),
        inputs={"stock_data": "stock_data_aapl"},
        outputs={"df_feat_engineered": "df_aapl_engineered"},
        namespace="feature_engineering_aapl",
    )


def create_fe_amzn(**kwargs) -> Pipeline:
    """Create the pipeline for feature engineering."""
    return pipeline(
        pipe=feature_engineering_template(**kwargs),
        inputs={"stock_data": "stock_data_amzn"},
        outputs={"df_feat_engineered": "df_amzn_engineered"},
        namespace="feature_engineering_amzn",
    )


def create_fe_msft(**kwargs) -> Pipeline:
    """Create the pipeline for feature engineering."""
    return pipeline(
        pipe=feature_engineering_template(**kwargs),
        inputs={"stock_data": "stock_data_msft"},
        outputs={"df_feat_engineered": "df_msft_engineered"},
        namespace="feature_engineering_msft",
    )


def create_fe_googl(**kwargs) -> Pipeline:
    """Create the pipeline for feature engineering."""
    return pipeline(
        pipe=feature_engineering_template(**kwargs),
        inputs={"stock_data": "stock_data_googl"},
        outputs={"df_feat_engineered": "df_googl_engineered"},
        namespace="feature_engineering_googl",
    )


def create_fe_blk(**kwargs) -> Pipeline:
    """Create the pipeline for feature engineering."""
    return pipeline(
        pipe=feature_engineering_template(**kwargs),
        inputs={"stock_data": "stock_data_blk"},
        outputs={"df_feat_engineered": "df_blk_engineered"},
        namespace="feature_engineering_blk",
    )
