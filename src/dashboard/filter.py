import streamlit as st
from pandas import DataFrame
from datetime import datetime


def get_ui_filter(df: DataFrame) -> tuple[dict[str, bool], datetime, datetime, int]:
    st.sidebar.header("Filters")

    # Toggle visibility of each chart section
    show = {
        "index": st.sidebar.checkbox("Index chart", True),
        "volatility": st.sidebar.checkbox("Volatility", True),
        "direct": st.sidebar.checkbox("Direct relationship", True),
        "correlation": st.sidebar.checkbox("Rolling correlation", True),
        "heatmap": st.sidebar.checkbox("Heatmap", True),
        "table": st.sidebar.checkbox("Stats table", True),
        "regression": st.sidebar.checkbox("Oil Regression", True),
    }

    # Date range slider bounded by available data
    start, end = st.sidebar.slider(
        "Time range",
        min_value=df.index.min().to_pydatetime(),
        max_value=df.index.max().to_pydatetime(),
        value=(df.index.min().to_pydatetime(), df.index.max().to_pydatetime())
    )

    # Number of trading days used for rolling calculations
    window = st.sidebar.slider("Rolling window (4)", 10, 120, 60)

    return show, start, end, window