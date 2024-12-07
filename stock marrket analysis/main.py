# Install necessary libraries
# pip install pandas numpy matplotlib yfinance seaborn

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch Stock Data
stock = yf.Ticker("AAPL")  # Replace 'AAPL' with the desired stock symbol
data = stock.history(period="6mo")  # Fetch last 1 year of data
print(data.head())

# Step 2: Visualize Closing Price
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title('Stock Closing Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Step 3: Calculate Moving Averages
data['20_MA'] = data['Close'].rolling(window=20).mean()
data['50_MA'] = data['Close'].rolling(window=50).mean()

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['20_MA'], label='20-Day MA', color='green')
plt.plot(data['50_MA'], label='50-Day MA', color='red')
plt.title('Stock Closing Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Step 4: Correlation Analysis (Optional)
returns = data['Close'].pct_change()
sns.histplot(returns, kde=True, bins=30)
plt.title('Stock Returns Distribution')
plt.show()



