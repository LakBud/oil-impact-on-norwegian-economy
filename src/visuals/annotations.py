from plotly.graph_objects import Figure


# Major geopolitical and macroeconomic events to overlay on charts
KEY_EVENTS = [
    ("2020-03-01", "COVID"),
    ("2022-02-24", "Ukraine War"),
    ("2023-10-07", "Israel-Hamas"),
    ("2025-01-20", "Trump 2.0"),
]


def add_event_lines(fig: Figure, rows: list[int], plot_type_map: list[str]) -> Figure:
    for date, label in KEY_EVENTS:
        first_xy_row = None

        for row, plot_type in zip(rows, plot_type_map):
            if plot_type != "xy":
                continue

            if first_xy_row is None:
                first_xy_row = row  # Track first xy row for annotation placement

            # Vertical dotted line spanning the full height of each xy subplot
            fig.add_shape(
                type="line",
                x0=date, x1=date,
                y0=0, y1=1,
                yref="y domain",
                line=dict(color="#f97316", width=1, dash="dot"),
                row=row,
                col=1,
            )

        # Add label once at the top, aligned to the first xy subplot
        if first_xy_row is not None:
            fig.add_annotation(
                x=date,
                y=1,
                yref="paper",
                text=label,
                showarrow=False,
                font=dict(color="#f97316", size=9),
                textangle=-90,
                xanchor="left",
                yanchor="top",
            )

    return fig