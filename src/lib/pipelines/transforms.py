from pandas import DataFrame


def calculate_returns(df: DataFrame) -> DataFrame:
    # Returns measure how much an asset gained or lost each day as a percentage
    # This makes assets comparable regardless of their actual price level
    # Formula: (current - previous) / previous
    return df.pct_change(fill_method=None).dropna()


def create_indexed(df: DataFrame) -> DataFrame:
    # Indexing rebases all assets to 100 at the start date
    # This lets you compare performance across assets with very different price scales
    # e.g. Oil at $80 vs EQNR at $30 — after indexing both start at 100
    return df / df.iloc[0] * 100