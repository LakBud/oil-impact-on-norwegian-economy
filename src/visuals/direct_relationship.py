import numpy as np
import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame


def add_direct_relationship(fig: Figure, df: DataFrame, row: int, x_col: str = "Oil", y_col: str = "NOKUSD") -> Figure:
    x = df[x_col]
    y = df[y_col]

    # Fit a linear trend line through the scatter points
    slope, intercept = np.polyfit(x, y, 1)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept

    # Raw daily returns as scatter points
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name=f"{y_col} vs {x_col}",
            opacity=0.5,
            legendgroup="direct",
            legendgrouptitle=dict(text="Oil vs NOK/USD"),
        ),
        row=row, col=1
    )

    # OLS regression line showing the overall directional relationship
    fig.add_trace(
        go.Scatter(
            x=x_line,
            y=y_line,
            mode="lines",
            name="Trend (Regression)",
            line=dict(color="red"),
            legendgroup="direct",
        ),
        row=row, col=1
    )

    fig.update_xaxes(title_text=f"{x_col} Returns", row=row, col=1)
    fig.update_yaxes(title_text=f"{y_col} Returns", row=row, col=1)

    return fig