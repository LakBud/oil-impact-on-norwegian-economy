from src.visuals.annotations import add_event_lines
from src.theme.theme import BG, ACCENT
from src.lib.dashboard.core import build_figure, add_traces, apply_legends
from src.theme.dashboard_styling import style_annotations, style_axes, build_legend_layout
from src.utils.dashboard_utils import compute_row_heights, detect_heatmaps
from plotly.graph_objects import Figure


def render_dashboard(layout: list[dict]) -> Figure:
    row_heights = compute_row_heights(layout)
    detect_heatmaps(layout, row_heights)  # Inject row_heights into heatmap meta before building

    fig = build_figure(layout)

    trace_map = add_traces(fig, layout)
    legend_map = apply_legends(fig, trace_map)

    # Overlay geopolitical event lines across all xy subplots
    add_event_lines(
        fig,
        list(range(1, len(layout) + 1)),
        [item["type"] for item in layout]
    )

    legend_layout = build_legend_layout(legend_map, len(layout))

    fig.update_layout(
        hovermode="x unified",
        height=600 * len(layout),  # Each panel gets a fixed 600px of height
        template="plotly_dark",
        margin=dict(l=80, r=220, t=80, b=60),
        paper_bgcolor=BG,
        plot_bgcolor=BG,
        font=dict(color=ACCENT),
        **legend_layout  # Unpack per-subplot legend positions
    )

    style_annotations(fig)
    style_axes(fig, layout)

    return fig