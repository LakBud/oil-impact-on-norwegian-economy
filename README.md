# Oil Prices effect in Norwegian Markets and NOK/USD

An interactive dashboard analyzing how changes in oil prices affect Norwegian stocks (EQNR, DNB, NHY) and the NOK/USD exchange rate.

---

## Table of Contents

- [Dataset Description](#dataset-description)
- [Analysis Choices](#analysis-choices)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Requirements](#requirements)

---

## Dataset Description

### Sources

All data is fetched via **yfinance**, which provides historical market data from Yahoo Finance with a 15-minute delay.

| Asset       | Ticker     | Description                      |
| ----------- | ---------- | -------------------------------- |
| Oil         | `BZ=F`     | Brent Crude Oil futures price    |
| Equinor     | `EQNR.OL`  | Oslo Børs: Equinor ASA           |
| DNB         | `DNB.OL`   | Oslo Børs: DNB Bank ASA          |
| Norsk Hydro | `NHY.OL`   | Oslo Børs: Norsk Hydro ASA       |
| NOK/USD     | `NOKUSD=X` | Norwegian Krone / US Dollar rate |

### Content

- **Period:** 10 years of daily closing prices
- **Processed data:** daily returns, indexed performance (base 100), rolling correlations, volatility, descriptive statistics

### Limitations

- Data is delayed by 15 minutes — not suitable for live trading
- yfinance data may have occasional gaps on Norwegian holidays; these are forward-filled
- Linear regression assumes a linear relationship between time and oil price, which is a simplification
- Correlation does not imply causation

---

## Analysis Choices

### 1. Indexed Performance

Prices are rebased to 100 at the start of the selected period, allowing direct comparison of relative performance across assets with different price scales.

### 2. Oil Volatility

Rolling 30-day standard deviation of oil returns, used as a proxy for market uncertainty. A higher value indicates more turbulent oil markets.

### 3. Oil vs NOK/USD (Direct Relationship)

A scatter plot with an OLS regression line showing the contemporaneous relationship between daily oil returns and NOK/USD returns. Norway's oil-dependent economy means these tend to move together.

### 4. Rolling Correlation

A 60-day rolling Pearson correlation between oil returns and each Norwegian asset, showing how the relationship evolves over time. Key events (e.g. COVID, Ukraine War) are marked as vertical lines.

### 5. Correlation Heatmap

A static correlation matrix across all assets for the full selected period, giving an overview of pairwise relationships.

### 6. Stats Table

Descriptive statistics for daily returns: mean, median, min, max, daily standard deviation, and annualized volatility (daily std × √252).

### 7. Oil Price Regression

A simple linear regression (scikit-learn) fitted on historical oil prices using time as the feature. Produces a fitted trend line and a 252-day (1 trading year) forward forecast with a 95% confidence interval. This is intentionally simple — the goal is to demonstrate the method, not to produce accurate price predictions.

---

## Project Structure

```
oil-impact-on-norwegian-economy/
├── src/
│   ├── dashboard/
│   │   ├── app.py          # Streamlit entry point
│   │   ├── data.py         # Dataset builder
│   │   ├── layout.py       # Chart layout definition
│   │   ├── render.py       # Plotly figure renderer
│   │   └── filter.py       # Sidebar controls
│   ├── lib/
│   │   ├── dashboard/
│   │   │   ├── core.py        # Plotly dashboard builders
│   │   ├── pipelines/
│   │   │   ├── fetch.py        # yfinance data fetching
│   │   │   ├── transforms.py   # Indexing, percent
│   │   │   ├── features.py     # Volatility, rolling correlation
│   │   │   └── regression.py   # Linear regression + forecasting
│   ├── pipelines/
│   │   ├── processed.py    # Main data pipeline
│   │   └── stocks.py       # Stock data pipeline
│   ├── reports/
│   │   ├── images.py
│   ├── theme/
│   │   ├── theme.py        # Color variables
│   │   ├── dashboard_styling.py # Dashboard component styling
│   ├── utils/
│   │   ├── dashboard_utils.py
│   └── visuals/
│       ├── annotations.py  # Key event lines
│       ├── correlation.py
│       ├── direct_relationship.py
│       ├── heatmap.py
│       ├── indexed.py
│       ├── regression.py
│       ├── stats_table.py
│       └── volatility.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── stats/
├── docs/
|   └── results.md      # Results of the analysis
|   └── results_nor.md
├── pyproject.toml
└── README.md
└── README_NOR.md
```

---

## How to Run

## Quick Start

```bash
pip install -r requirements.txt
python -m src.pipelines.processed
streamlit run src/dashboard/app.py
```

---

## Running the Project

### 1. Clone the repository

```bash
git clone <repo-url>
cd oil-impact-on-norwegian-economy
```

### 2. Install dependencies

Using pip:

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv sync
```

### 3. Run the data pipeline

This fetches data from yfinance and generates all processed CSV files.

Using pip:

```bash
python -m src.pipelines.processed
```

Or using uv:

```bash
uv run python -m src.pipelines.processed
```

### 4. Launch the dashboard

Using pip:

```bash
streamlit run src/dashboard/app.py
```

Or using uv:

```bash
uv run streamlit run src/dashboard/app.py
```

The dashboard will open at:

```text
http://localhost:8501
```

### 5. Refresh data

The dashboard automatically refreshes every 15 minutes. You can also manually refresh the application using the **Rerun** button in the Streamlit interface.

---

## Requirements

- Python 3.11+

Optional:

- uv (for users who want to install and run the project using uv)

Essential dependencies:

- streamlit
- plotly
- pandas
- numpy
- scikit-learn
- yfinance

---
