import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame


def add_corr(fig: Figure, df: DataFrame, row: int, cols: list[str], title: str = "Rolling Correlation") -> None:
    # Skip columns not present in the dataframe
    valid_cols = [c for c in cols if c in df.columns]

    if not valid_cols:
        return

    for i, col in enumerate(valid_cols):
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df[col],
                mode="lines",
                name=col,
                legendgroup=f"corr_{col}",
                legendgrouptitle=dict(text=title) if i == 0 else None,  # Title only on first trace
            ),
            row=row,
            col=1
        )

    fig.update_xaxes(title_text="Date", row=row, col=1)
    fig.update_yaxes(title_text="Correlation", row=row, col=1)