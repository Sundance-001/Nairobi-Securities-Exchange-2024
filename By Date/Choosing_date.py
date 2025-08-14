# Analysis by date
#For 210 days
from Numerical_Cleaning import*
import os
grouped_date = df_numeric_only.groupby('Date')
all_dates = df_numeric_only['Date'].sort_values().unique()
print(f'Available dates {all_dates[0]} to {all_dates[-1]}')
date_str = input("Enter the date in YYYY-MM-DD format: ")
try:
    target_date = pd.Timestamp(date_str)
    df_on_date = grouped_date.get_group(target_date)
    file_name = (f'{target_date.date()}.csv')
    output_folder = "Date_files_csv's"
    os.makedirs(output_folder, exist_ok=True)
    file_path = os.path.join(output_folder, f'{target_date.date()}.csv')
    df_on_date.to_csv(file_path, index=False)
    print(f"File saved as {file_path}")
except KeyError:
    print(f"No data found for {date_str}. Please check the date and try again.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
    
    