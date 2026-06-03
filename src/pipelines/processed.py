import pandas as pd
import os
from src.lib.pipelines.fetch import download_prices
from src.lib.pipelines.transforms import create_indexed, calculate_returns
from src.lib.pipelines.features import add_volatility, rolling_corr
from src.lib.pipelines.regression import fit_oil_regression


# Data folder structure
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("data/stats", exist_ok=True)

#-------------------------------
# Fetch data (RAW)
#-------------------------------
tickers = {
    "Oil":    "BZ=F",
    "EQNR":   "EQNR.OL",
    "DNB":    "DNB.OL",
    "NHY":    "NHY.OL",
    "NOKUSD": "NOKUSD=X",
}

# Download
raw = download_prices(tickers, period="10y")

# Extract closing price per asset
# closing price = last traded price of each session
frames = {}
for name, ticker in tickers.items():
    frames[name] = raw[ticker]["Close"]

raw_df = pd.DataFrame(frames)

#-------------------------------
# Clean data
#-------------------------------

# Sort, forward-fill missing trading days (e.g. holidays), then drop any remaining NaNs
raw_df = raw_df.sort_index().ffill().dropna()

# -------------------------------
# Transformations
# -------------------------------

# Percent changes
returns_df = calculate_returns(raw_df)

# Keep a separate copy before adding features, used for pure return-based analysis
returns_analysis = returns_df.copy()

# 30-day rolling volatility added as a new column to returns_df
returns_df = add_volatility(returns_df, col="Oil", window=30)

# Price-based transformations (uses raw data)
indexed_df = create_indexed(raw_df)

# Correlation measures how strongly two assets move together (-1 = opposite, 0 = no relationship, 1 = in sync)
corr_df = returns_analysis.corr()

# 60-day rolling correlation of each asset against oil
rolling_corr_df = rolling_corr(
    returns_df,
    base="Oil",
    cols=["EQNR", "DNB", "NHY", "NOKUSD"],
    window=60
)

oil_actual, oil_fitted, oil_forecast = fit_oil_regression(raw_df)

regression_df = pd.DataFrame({
    "Actual": oil_actual,
    "Fitted": oil_fitted,
}).dropna()

#-------------------------------
# Statistical analysis
#-------------------------------

# Calculate descriptive statistics for stock returns
stats = pd.DataFrame({
    "mean": returns_analysis.mean(), # Average daily return
    "median": returns_analysis.median(), # Middle value, robust to outliers
    "min": returns_analysis.min(), # Worst single-day return
    "max": returns_analysis.max(), # Best single-day return
    "std": returns_analysis.std(),  # How much returns deviate from the mean on average (risk measure)
    "annualized_std": returns_analysis.std() * (252 ** 0.5), # Daily volatility scaled to yearly
})
#-------------------------------
# Save data into csv
#-------------------------------
raw_df.to_csv("data/raw/raw_prices.csv")


returns_df.to_csv("data/processed/returns.csv")
indexed_df.to_csv("data/processed/indexed.csv")
rolling_corr_df.to_csv("data/processed/rolling_corr.csv")
returns_df[["Oil_volatility"]].to_csv("data/processed/oil_volatility.csv")
regression_df.to_csv("data/processed/regression.csv")
oil_forecast.to_csv("data/processed/oil_forecast.csv")

stats.to_csv("data/stats/descriptive_stats.csv")
corr_df.to_csv("data/stats/correlation_matrix.csv")



print("processed.py is finished. Files saved in data/raw, data/processed/ and data/stats/")