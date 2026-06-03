import pandas as pd
from pandas import DataFrame
from src.lib.pipelines.features import rolling_corr


def build_datasets(
    returns_df: DataFrame,
    indexed_df: DataFrame,
    corr_df: DataFrame,
    stats: DataFrame,
    regression_df: DataFrame,
    oil_forecast: DataFrame,
    start: str,
    end: str,
    window: int
) -> dict[str, DataFrame]:
    # Filter returns and indexed prices to the user-selected date range
    returns = returns_df.loc[start:end]
    indexed = indexed_df.loc[start:end]

    # Recompute rolling correlation based on the selected window and date range
    rolling = rolling_corr(
        returns,
        base="Oil",
        cols=["EQNR", "DNB", "NHY", "NOKUSD"],
        window=window
    )

    # Combine historical regression fit with the forward forecast into one series
    regression = pd.concat([
        regression_df,
        oil_forecast.rename("Forecast")
    ])

    return {
        "returns": returns,
        "indexed": indexed,
        "corr": corr_df,        # Full correlation matrix (not date-filtered)
        "rolling_corr": rolling,
        "stats": stats,         # Full stats (not date-filtered)
        "regression": regression
    }