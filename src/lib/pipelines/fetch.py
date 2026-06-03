import yfinance as yf
from pandas import DataFrame


def download_prices(tickers: dict[str, str], period: str = "5y") -> DataFrame:
    data = yf.download(
        list(tickers.values()),
        period=period,
        auto_adjust=True,  # Adjusts for splits and dividends
        group_by="ticker", # Organizes columns by ticker symbol
    )

    if data.empty:
        raise ValueError("No data downloaded from Yahoo Finance")

    return data