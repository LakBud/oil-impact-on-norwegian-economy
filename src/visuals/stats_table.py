import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame
from src.theme.theme import ORANGE, ACCENT, BG, BG_ALT


def add_stats_table(fig: Figure, stats_df: DataFrame, row: int) -> Figure:
    formatted = stats_df.copy()

    # Format all return/volatility columns as percentages
    pct_cols = ["mean", "median", "min", "max", "std", "annualized_std"]
    for col in pct_cols:
        formatted[col] = formatted[col].map(lambda x: f"{x:.2%}")

    # Alternate row background colors for readability
    n_rows = len(formatted)
    row_colors = [[BG if i % 2 == 0 else BG_ALT for i in range(n_rows)]]

    fig.add_trace(
        go.Table(
            header=dict(
                values=[
                    "Asset", "Mean Return", "Median",
                    "Min", "Max", "Daily Std", "Ann. Volatility"
                ],
                fill_color=ORANGE,
                font=dict(color=BG, size=12),
                align="center",
                height=33
            ),
            cells=dict(
                values=[
                    formatted.index.tolist(),
                    formatted["mean"].tolist(),
                    formatted["median"].tolist(),
                    formatted["min"].tolist(),
                    formatted["max"].tolist(),
                    formatted["std"].tolist(),
                    formatted["annualized_std"].tolist(),
                ],
                fill_color=row_colors * 7,  # Repeat color pattern across all columns
                font=dict(color=ACCENT, size=11),
                align="center",
                height=28,
                line=dict(color=ORANGE, width=0.3),
            )
        ),
        row=row,
        col=1
    )

    return fig