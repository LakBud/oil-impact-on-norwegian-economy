import pandas as pd
from pandas import DataFrame


def add_volatility(df: DataFrame, col: str = "Oil", window: int = 30) -> DataFrame:
    # Volatility measures how much an asset's return deviates from its average
    # High volatility = large price swings, low volatility = stable price movement
    df[f"{col}_volatility"] = df[col].rolling(window).std() * (252 ** 0.5)
    return df


def rolling_corr(df: DataFrame, base: str = "Oil", cols: list[str] = None, window: int = 60) -> DataFrame:
    if cols is None:
        cols = ["EQNR", "DNB", "NHY", "NOKUSD"]

    out = pd.DataFrame()
    for c in cols:
        # Rolling = computed over a moving time window rather than the full dataset
        # Correlation here shows how closely each stock moves with oil over time
        # A value of 1 = moves perfectly with oil, -1 = moves opposite, 0 = no relationship
        out[c] = df[base].rolling(window).corr(df[c])

    return out.dropna()