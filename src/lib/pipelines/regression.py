import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from pandas import DataFrame, Series


# Convert dates to ordinal integers so sklearn can use them as numeric features
def _to_X(index: pd.DatetimeIndex) -> np.ndarray:
    return index.map(pd.Timestamp.toordinal).values.reshape(-1, 1)


def fit_oil_regression(raw_df: DataFrame, forecast_days: int = 720) -> tuple[Series, Series, Series]:
    prices = raw_df["Oil"].dropna()

    # Linear regression finds the best-fit straight line through the price history
    # It learns the overall long-term trend, ignoring short-term noise
    model = LinearRegression().fit(_to_X(prices.index), prices.values)

    # Fitted = what the trend line predicts for dates we already have data for
    fitted = pd.Series(model.predict(_to_X(prices.index)), index=prices.index, name="Fitted")

    # Forecast = extending that same trend line into future dates we don't have yet
    future_dates = pd.bdate_range(start=prices.index[-1], periods=forecast_days + 1)[1:]
    forecast = pd.Series(model.predict(_to_X(future_dates)), index=future_dates, name="Forecast")

    return prices.rename("Actual"), fitted, forecast