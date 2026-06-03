from src.theme.theme import ORANGE, GRID, ACCENT
from plotly.graph_objects import Figure


DASHBOARD_STYLE: str = """
    <style>
        .stApp, .stApp > div, section[data-testid="stSidebar"],
        .block-container, header, footer {
            background-color: #0a0a0a !important;
            color: #e0e0e0 !important;
        }
        h1, h2, h3, p, label, span, div {
            color: #e0e0e0 !important;
        }
        .stSelectbox, .stMultiSelect, .stSlider, .stDateInput {
            background-color: #0a0a0a !important;
        }
        h1 { text-align: center !important; }
        
        section[data-testid="stSidebar"] {
    background-color: #0a0a0a !important;
    border-right: 1px solid #2a2a2a !important;
    
        [data-testid="stSlider"] div[role="slider"] {
        background-color: #f97316 !important;
    }
    [data-testid="stSlider"] > div > div > div {
        background-color: #f97316 !important;
    }

    </style>
"""


def style_annotations(fig: Figure) -> None:
    # Style subplot titles — center them and apply consistent font
    for ann in fig.layout.annotations:
        ann.font.update(size=20, color=ORANGE)
        if ann.xref == "paper":
            ann.update(x=0.5, xanchor="center")


def style_axes(fig: Figure, layout: list[dict]) -> None:
    # Apply consistent axis styling to all xy subplots
    for row, item in enumerate(layout, start=1):
        if item["type"] != "xy":
            continue  # Skip tables and other non-xy types

        fig.update_xaxes(
            gridcolor=GRID,
            linecolor=GRID,
            tickfont=dict(color=ACCENT, size=10),
            zeroline=False,
            row=row,
            col=1,
        )

        fig.update_yaxes(
            gridcolor=GRID,
            linecolor=GRID,
            tickfont=dict(color=ACCENT, size=10),
            zeroline=False,
            row=row,
            col=1,
        )


def build_legend_layout(legend_map: dict[str, int], total_rows: int) -> dict[str, dict]:
    # Position each legend box to the right of its corresponding subplot
    return {
        key: dict(
            x=1.02,
            y=1 - (row - 0.8) / total_rows,  # Vertical position derived from row number
            xanchor="left",
            yanchor="top",
            bgcolor="rgba(255,255,255,0.03)",
            bordercolor=ORANGE,
            borderwidth=1,
            font=dict(color=ACCENT, size=10),
        )
        for key, row in legend_map.items()
    }