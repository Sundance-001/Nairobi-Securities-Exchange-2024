# 
import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\nse_numeric_only.csv')

# Ensure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Function to get stock summary
def get_stock_summary(stock_code):
    stock_data = df[df['Code'].str.upper() == stock_code.upper()]
    if stock_data.empty:
        return f"No data found for stock code: {stock_code}"
    
    # Remove rows with NaN prices before finding min/max
    if stock_data['Day Price_num'].notna().any():
        lowest_price_row = stock_data.loc[stock_data['Day Price_num'].idxmin()]
        highest_price_row = stock_data.loc[stock_data['Day Price_num'].idxmax()]
    else:
        lowest_price_row = highest_price_row = None
    
    # Check for volatility values
    if stock_data['Change%_num'].notna().any():
        most_volatile_row = stock_data.loc[stock_data['Change%_num'].abs().idxmax()]
    else:
        most_volatile_row = None
    
    summary = {
        "Stock Code": stock_code.upper(),
        "Company Name": stock_data['Name'].iloc[0],
        "Average Price": stock_data['Day Price_num'].mean(),
        "Median Price": stock_data['Day Price_num'].median(),
        "Price Std Dev": stock_data['Day Price_num'].std(),
        "Lowest Price": lowest_price_row['Day Price_num'] if lowest_price_row is not None else None,
        "Lowest Price Date": lowest_price_row['Date'].date() if lowest_price_row is not None else None,
        "Highest Price": highest_price_row['Day Price_num'] if highest_price_row is not None else None,
        "Highest Price Date": highest_price_row['Date'].date() if highest_price_row is not None else None,
        "Average % Change": stock_data['Change%_num'].mean(),
        "Most Volatile % Change": most_volatile_row['Change%_num'] if most_volatile_row is not None else None,
        "Most Volatile Date": most_volatile_row['Date'].date() if most_volatile_row is not None else None,
        "Total Volume": stock_data['Volume_num'].sum(),
        "Max Volume": stock_data['Volume_num'].max(),
        "12m Low": stock_data['12m Low_num'].iloc[0],
        "12m High": stock_data['12m High_num'].iloc[0]
    }
    
    return summary
while True:
    code_input = input("Enter stock code (or 'q' to quit): ").strip()
    if code_input.lower() == 'q':
        print("Exiting program.")
        break

    result = get_stock_summary(code_input)

    # Display results
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)

    print("-" * 40)  # Divider for readability

