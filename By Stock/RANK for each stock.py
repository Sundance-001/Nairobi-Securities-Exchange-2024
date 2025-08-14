import pandas as pd
import numpy as np

# === Load CSV ===
df = pd.read_csv(r'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\nse_numeric_only.csv')

# Ensure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# === Group by stock code and aggregate statistics ===
grouped_by_code = df.groupby('Code').agg({
    'Day Price_num': ['mean', 'median', 'std', 'min', 'max'],
    'Change%_num': ['mean', 'std'],
    'Volume_num': ['mean', 'sum', 'max'],
    '12m Low_num': 'first',
    '12m High_num': 'first',
    'Name': 'first'
}).reset_index()

# Flatten multi-level column names
grouped_by_code.columns = [
    '_'.join(col).strip('_') for col in grouped_by_code.columns.values
]

# === Create ranking columns for benchmarks ===
metrics_to_rank = [
    'Day Price_num_mean',
    'Change%_num_mean',
    'Volume_num_mean'
]

for metric in metrics_to_rank:
    grouped_by_code[f'{metric}_rank'] = (
        grouped_by_code[metric]
        .rank(ascending=False, method='min')
        .astype('Int64')  # Nullable integer type to allow NaN
    )

# Save grouped data
grouped_by_code.to_csv("stocks_grouped_by_code.csv", index=False)
print("Grouped dataset saved as 'stocks_grouped_by_code.csv'.")

# === Interactive ranking lookup with loop ===
while True:
    stock_code_input = input("\nEnter the stock code to view its rankings (or 'q' to quit): ").strip().upper()
    
    if stock_code_input.lower() == 'q':
        print("Exiting. Goodbye!")
        break

    if stock_code_input in grouped_by_code['Code'].values:
        stock_row = grouped_by_code[grouped_by_code['Code'] == stock_code_input]
        print("\n=== Stock Information & Rankings ===")
        print(f"Name: {stock_row['Name_first'].values[0]}")
        print(f"Average Price Rank: {stock_row['Day Price_num_mean_rank'].values[0]}")
        print(f"Average % Change Rank: {stock_row['Change%_num_mean_rank'].values[0]}")
        print(f"Average Volume Rank: {stock_row['Volume_num_mean_rank'].values[0]}")
    else:
        print("Stock code not found in dataset.")
