from plotly.subplots import make_subplots
from plotly.graph_objects import Figure
from src.theme.theme import LEGENDS
from src.theme.dashboard_styling import PANEL_HEIGHTS




def build_figure(layout: list[dict]) -> Figure:
    n = len(layout)
    
    row_heights = [PANEL_HEIGHTS.get(item["type"], 0.15) for item in layout]
    total = sum(row_heights)
    row_heights = [h / total for h in row_heights]

    return make_subplots(
        rows=n,
        cols=1,
        specs=[[{"type": item["type"]}] for item in layout],
        subplot_titles=[item["title"] for item in layout],
        vertical_spacing=min(0.04 * (7 / n), 0.15),
        row_heights=row_heights
    )

def add_traces(fig: Figure, layout: list[dict]) -> dict[int, int]:
    trace_map = {}  # Maps trace index -> row number

    for row, item in enumerate(layout, start=1):
        fn = item["fn"]
        df = item["df"]
        meta = item.get("meta", {})

        if not isinstance(meta, dict):
            meta = {}

        before = len(fig.data)
        fn(fig, df, row=row, **meta)

        # Record which row each newly added trace belongs to
        for i in range(before, len(fig.data)):
            trace_map[i] = row

    return trace_map


def apply_legends(fig: Figure, trace_map: dict[int, int]) -> dict[str, int]:
    legend_map = {}  # Maps legend key -> row number

    for i, trace in enumerate(fig.data):
        if getattr(trace, "type", None) == "table":
            continue  # Tables don't use legends

        row = trace_map.get(i, 1)
        legend_key = LEGENDS[min(row - 1, len(LEGENDS) - 1)]

        trace.legend = legend_key
        legend_map[legend_key] = row

    return legend_map