import yfinance as yf
import os

os.makedirs("data/raw", exist_ok=True)

# Stocks
oil = yf.download("BZ=F", period="10y")
eqnr = yf.download("EQNR.OL", period="10y")
dnb = yf.download("DNB.OL", period="10y")
nhy = yf.download("NHY.OL", period="10y")
nokusd = yf.download("NOKUSD=X", period="10y")

# Save to CSV to check data
oil.to_csv("data/raw/stocks/oil.csv")
eqnr.to_csv("data/raw/stocks/eqnr.csv")
dnb.to_csv("data/raw/stocks/dnb.csv")
nhy.to_csv("data/raw/stocks/nhy.csv")
nokusd.to_csv("data/raw/stocks/nokusd.csv")