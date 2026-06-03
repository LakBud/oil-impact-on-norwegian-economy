def compute_row_heights(layout: list[dict]) -> list[float]:
    # Tables get less space; xy plots get more
    heights = [
        1.2 if item["type"] == "xy" else 0.9
        for item in layout
    ]
    # Normalize so all heights sum to 1
    total = sum(heights)
    return [h / total for h in heights]


def detect_heatmaps(layout: list[dict], row_heights: list[float]) -> None:
    # Pass row_heights into heatmap meta so it can scale itself correctly
    for entry in layout:
        fn = entry.get("fn") if isinstance(entry, dict) else entry[1]

        if fn.__name__ == "add_heatmap":
            entry["meta"]["row_heights"] = row_heights