import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
DATA_PATH = r'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\nse_numeric_only.csv'
df = pd.read_csv(DATA_PATH)

# Ensure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Base directory for charts (same as CSV file location)
DATA_DIR = os.path.dirname(DATA_PATH)
CHARTS_BASE = os.path.join(DATA_DIR, "charts")

def plot_stock_metrics(stock_code):
    stock_data = df[df['Code'].str.upper() == stock_code.upper()]
    if stock_data.empty:
        print(f"No data found for stock code: {stock_code}")
        return
    
    stock_data = stock_data.sort_values('Date')

    # Prepare output folder inside NSE dataset folder
    stock_folder = os.path.join(CHARTS_BASE, stock_code.upper())
    os.makedirs(stock_folder, exist_ok=True)

    plt.style.use('seaborn-v0_8')

    # 1. Price Trend
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Date'], stock_data['Day Price_num'], marker='o', label='Closing Price')
    plt.title(f"{stock_code.upper()} - Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(stock_folder, "price_trend.png"))
    plt.close()

    # 2. Volume Traded
    plt.figure(figsize=(10, 5))
    plt.bar(stock_data['Date'], stock_data['Volume_num'], color='orange')
    plt.title(f"{stock_code.upper()} - Volume Traded")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.savefig(os.path.join(stock_folder, "volume_traded.png"))
    plt.close()

    # 3. Daily % Change
    plt.figure(figsize=(10, 5))
    plt.bar(stock_data['Date'], stock_data['Change%_num'], color='green')
    plt.axhline(0, color='red', linestyle='--')
    plt.title(f"{stock_code.upper()} - Daily % Change")
    plt.xlabel("Date")
    plt.ylabel("% Change")
    plt.savefig(os.path.join(stock_folder, "daily_percent_change.png"))
    plt.close()

    # 4. Price vs. 12-Month High/Low
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Date'], stock_data['Day Price_num'], label='Price', color='blue')
    plt.plot(stock_data['Date'], stock_data['12m High_num'], label='12m High', color='red', linestyle='--')
    plt.plot(stock_data['Date'], stock_data['12m Low_num'], label='12m Low', color='green', linestyle='--')
    plt.fill_between(stock_data['Date'], stock_data['12m Low_num'], stock_data['12m High_num'], color='gray', alpha=0.2)
    plt.title(f"{stock_code.upper()} - Price vs 12m High/Low")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.savefig(os.path.join(stock_folder, "price_vs_12m_range.png"))
    plt.close()

    # 5. Price Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(stock_data['Day Price_num'].dropna(), bins=20, color='purple', alpha=0.7)
    plt.title(f"{stock_code.upper()} - Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(stock_folder, "price_distribution.png"))
    plt.close()

    print(f"Charts saved in: {stock_folder}")

if __name__ == "__main__":
    while True:
        code = input("Enter stock code (or 'q' to quit): ").strip()
        if code.lower() == 'q':
            break
        plot_stock_metrics(code)
