import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame
from src.theme.theme import ORANGE, ACCENT, BG


def add_heatmap(fig: Figure, corr_df: DataFrame, row: int, **meta) -> Figure:
    fig.add_trace(
        go.Heatmap(
            z=corr_df.values,
            x=corr_df.columns,
            y=corr_df.index,
            # Blue = negative correlation, dark = neutral, orange = positive
            colorscale=[
                [0.0, "#1a6b8a"],
                [0.5, BG],
                [1.0, "#c2570a"],
            ],
            zmin=-1,
            zmax=1,
            showscale=True,
            name="Correlation",
            colorbar=dict(
                tickfont=dict(color=ACCENT),
                title=dict(text="Corr", font=dict(color=ACCENT)),
                bgcolor=BG,
                bordercolor=ORANGE,
                borderwidth=1,
            )
        ),
        row=row,
        col=1,
    )

    # Align colorbar vertically to its subplot rather than the full figure
    yaxis = f"yaxis{'' if row == 1 else row}"
    y_domain = fig.layout[yaxis].domain

    fig.data[-1].colorbar.y = sum(y_domain) / 2          # Center on subplot
    fig.data[-1].colorbar.len = (y_domain[1] - y_domain[0]) * 0.9  # Match subplot height
    fig.data[-1].colorbar.yanchor = "middle"

    return fig