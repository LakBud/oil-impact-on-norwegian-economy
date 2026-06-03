import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame


def add_volatility(fig: Figure, df: DataFrame, row: int) -> Figure:
    # Annualized rolling volatility derived from oil daily returns
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Oil_volatility"],
            name="Oil Volatility",
            legendgroup="volatility",
            legendgrouptitle=dict(text="Oil Volatility"),
        ),
        row=row,
        col=1
    )

    fig.update_xaxes(title_text="Date", row=row, col=1)
    fig.update_yaxes(title_text="Volatility", row=row, col=1)

    return fig