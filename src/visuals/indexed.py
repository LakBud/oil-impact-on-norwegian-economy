import plotly.graph_objects as go
from plotly.graph_objects import Figure
from pandas import DataFrame


def add_indexed(fig: Figure, df: DataFrame, row: int = 1) -> Figure:
    for col in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df[col],
                name=col,
                legendgroup=f"indexed_{col}",
                # Only show legend group title on the first trace
                legendgrouptitle=dict(text="Indexed Performance") if col == df.columns[0] else None,
            ),
            row=row,
            col=1
        )

    fig.update_xaxes(title_text="Date", row=row, col=1)
    fig.update_yaxes(title_text="Indexed (Start = 100)", row=row, col=1)

    return fig