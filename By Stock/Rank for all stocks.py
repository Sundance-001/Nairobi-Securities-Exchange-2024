# Grouping by code.py
# t avoid tight coupling data will be grouped in this file
# this file is independent from the file Grouping by Code.py
# However it is dependent on the nse_numeric_only.csv which makes it dependent on the file"Numerical cleaning .py" from the "By Date Folder
import pandas as pd
#Load and prepare data
df = pd.read_csv(
    r'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\nse_numeric_only.csv'
)

# Ensure Date is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# === Group by stock code and compute statistics ===
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

# === Summary & Ranking Analysis ===
def get_top_bottom(data, column, N=5):
    """Return top N and bottom N rows based on a column."""
    top_n = data.nlargest(N, column)
    bottom_n = data.nsmallest(N, column)
    return top_n, bottom_n

# Rank by different metrics
metrics = {
    'Average Price': 'Day Price_num_mean',
    'Volatility (Price Std Dev)': 'Day Price_num_std',
    'Volatility (% Change Std Dev)': 'Change%_num_std',
    'Average Volume': 'Volume_num_mean'
}

ranking_results = {}
for metric_name, col in metrics.items():
    top, bottom = get_top_bottom(grouped_by_code, col, N=5)
    ranking_results[metric_name] = {
        'Top 5': top,
        'Bottom 5': bottom
    }

# === Save outputs ===
# This outputs a csv similar to the one from Grouping by code.py
grouped_by_code.to_csv(
    r'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\stocks_grouped_by_code.csv',
    index=False
)

# Also save ranking summaries
for metric_name, result in ranking_results.items():
    result['Top 5'].to_csv(
        rf'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\top5_{metric_name.replace(" ", "_")}.csv',
        index=False
    )
    result['Bottom 5'].to_csv(
        rf'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\bottom5_{metric_name.replace(" ", "_")}.csv',
        index=False
    )

# === Print quick preview ===
print("=== Grouped Summary ===")
print(f"The first five aggregated values from the grouped stocks {grouped_by_code.head()}")
print("\n=== Ranking Results Preview ===")
for metric_name, result in ranking_results.items():
    print(f"\n{metric_name} - Top 5:")
    print(result['Top 5'][['Code', 'Name_first', metrics[metric_name]]])
    print(f"\n{metric_name} - Bottom 5:")
    print(result['Bottom 5'][['Code', 'Name_first', metrics[metric_name]]])
