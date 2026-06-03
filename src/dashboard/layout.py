from typing import Callable
from pandas import DataFrame
from src.visuals.indexed import add_indexed
from src.visuals.correlation import add_corr
from src.visuals.volatility import add_volatility
from src.visuals.heatmap import add_heatmap
from src.visuals.stats_table import add_stats_table
from src.visuals.direct_relationship import add_direct_relationship
from src.visuals.regression import add_regression


# Static definition of all available panels in display order
LAYOUT_DEFINITION = [
    {
        "key": "index",
        "title": "Indexed Performance",
        "fn": add_indexed,
        "data": "indexed",
        "type": "xy",
    },
    {
        "key": "volatility",
        "title": "Oil Volatility",
        "fn": add_volatility,
        "data": "returns",
        "type": "xy",
    },
    {
        "key": "direct",
        "title": "Oil vs NOK/USD",
        "fn": add_direct_relationship,
        "data": "returns",
        "type": "xy",
    },
    {
        "key": "correlation",
        "title": "Rolling Correlation",
        "fn": add_corr,
        "data": "rolling_corr",
        "type": "xy",
        "meta": {
            "cols": ["EQNR", "DNB", "NHY", "NOKUSD"]
        }
    },
    {
        "key": "heatmap",
        "title": "Correlation Heatmap",
        "fn": add_heatmap,
        "data": "corr",
        "type": "xy",
    },
    {
        "key": "table",
        "title": "Stats Table",
        "fn": add_stats_table,
        "data": "stats",
        "type": "table",
    },
    {
        "key": "regression",
        "title": "Oil Price Regression",
        "fn": add_regression,
        "data": "regression",
        "type": "xy",
    },
]


def build_layout(show_map: dict[str, bool], data: dict[str, DataFrame]) -> list[dict]:
    layout = []

    for cfg in LAYOUT_DEFINITION:
        # Skip panels the user has toggled off
        if not show_map.get(cfg["key"], False):
            continue

        layout.append({
            "title": cfg["title"],
            "fn": cfg["fn"],
            "df": data[cfg["data"]],
            "meta": cfg.get("meta", {}),
            "type": cfg["type"],
        })

    # Prefix each visible panel title with its display order number
    for i, item in enumerate(layout, start=1):
        item["title"] = f"{i}. {item['title']}"

    return layout