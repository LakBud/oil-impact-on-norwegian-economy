import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame
from src.theme.theme import ORANGE, ACCENT


def add_regression(fig: Figure, df: DataFrame, row: int) -> Figure:
    actual = df["Actual"].dropna()
    fitted = df["Fitted"].dropna()
    forecast = df["Forecast"].dropna()

    # Historical oil price
    fig.add_trace(
        go.Scatter(
            x=actual.index,
            y=actual,
            name="Oil Price (Actual)",
            mode="lines",
            line=dict(color=ACCENT, width=1),
            legendgroup="regression",
            legendgrouptitle=dict(text="Oil Regression"),
        ),
        row=row, col=1
    )

    # OLS trend line fitted to historical data
    fig.add_trace(
        go.Scatter(
            x=fitted.index,
            y=fitted,
            name="Linear Trend",
            mode="lines",
            line=dict(color=ORANGE, width=2, dash="dash"),
            legendgroup="regression",
        ),
        row=row, col=1
    )

    # Forward projection continuing the fitted trend
    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast,
            name="Forecast (365 business days)",
            mode="lines",
            line=dict(color="#c2570a", width=2, dash="dot"),
            legendgroup="regression",
        ),
        row=row, col=1
    )

    # Set x-axis range to span full history and forecast period
    fig.update_xaxes(
        range=[
            str(actual.index[0]),
            str(forecast.index[-1])
        ],
        row=row, col=1
    )
    fig.update_yaxes(title_text="Oil Price (USD)", row=row, col=1)

    return fig