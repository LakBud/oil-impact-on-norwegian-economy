import streamlit as st
from streamlit_autorefresh import st_autorefresh

from src.pipelines.processed import (
    returns_df,
    indexed_df,
    corr_df,
    stats,
    regression_df,
    oil_forecast
)

from src.dashboard.filter import get_ui_filter
from src.dashboard.data import build_datasets
from src.dashboard.layout import build_layout
from src.dashboard.render import render_dashboard
from src.theme.dashboard_styling import DASHBOARD_STYLE


st_autorefresh(interval=900_000)  # Refresh every 15 minutes to pick up new market data

st.set_page_config(
    page_title="Oil & Norwegian Market Dashboard",
    layout="wide"
)

st.markdown(DASHBOARD_STYLE, unsafe_allow_html=True)

st.title("How Oil Prices affect Norwegian Markets and NOK/USD")

# Sidebar filters: which charts to show, date range, and rolling window size
show_map, start_date, end_date, window = get_ui_filter(returns_df)

# Slice and prepare all dataframes based on user filters
data = build_datasets(
    returns_df,
    indexed_df,
    corr_df,
    stats,
    regression_df,
    oil_forecast,
    start_date,
    end_date,
    window
)

layout = build_layout(show_map, data)

if not layout:
    st.warning("Select at least one chart to display.")
    st.stop()

fig = render_dashboard(layout)

st.plotly_chart(fig, width="stretch")


# uv run python -m streamlit run src/dashboard/app.py
# python -m streamlit run src/dashboard/app.py