#Groping by code
# Generates a csv file with info about all the stocks
#This from the already cleaned nse_numeric_only.csv file
#The csv from which all subsequent analysis will be performed is saved as stocks_grouped_by_code.csv
import pandas as pd
# Load CSV
df = pd.read_csv(r'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\nse_numeric_only.csv')

# Ensure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Group by stock code and aggregate statistics
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
# Save grouped data
grouped_by_code.to_csv("stocks_grouped_by_code.csv", index=False)
print(f'Aggregated values for every sockin the time period is saved in a file "stocks_grouped_by_code.csv"')
print(f' Success, here is a list of the first five stocks {grouped_by_code.head()}')
