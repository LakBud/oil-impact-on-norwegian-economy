from plotly.subplots import make_subplots
from plotly.graph_objects import Figure
from src.theme.theme import LEGENDS


def build_figure(layout: list[dict]) -> Figure:
    # Tables need less vertical space than charts
    row_heights = [
        0.06 if item["type"] == "table" else 0.15
        for item in layout
    ]

    return make_subplots(
        rows=len(layout),
        cols=1,
        specs=[[{"type": item["type"]}] for item in layout],
        subplot_titles=[item["title"] for item in layout],
        vertical_spacing=0.03,
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