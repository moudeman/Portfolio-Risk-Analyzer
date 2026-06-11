import pandas as pd
import numpy as np
import yfinance as yf

print("pandas:", pd.__version__)
print("numpy :", np.__version__)

# Pull one week of Apple prices as a live connectivity test
data = yf.download("AAPL", period="5d")
print("\nLast 5 days of AAPL closing prices:")
print(data["Close"])
print("\n✅ Everything works. You're ready to build.")

data_NVDA  = yf.download("NVDA", period="10d")
print("\nLast 10 days of Nvidia closing prices:")
print(data_NVDA["Close"])

git init
git remote add origin https://github.com/moudeman/Portfolio-Risk-Analyzer
git branch -M main
git pull origin main