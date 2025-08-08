#Cleaning
import numpy as np
import pandas as pd
from insepection import df # module where df is dedfined
pd.set_option('future.no_silent_downcasting', True)

def clean_numeric_series(s, percent = False):
    s = s.astype(str).str.strip()
    s = s.str.replace(',', '', regex = False)
    s = s.str.replace('+', '', regex = False)
    if percent:
        s = s.str.replace('%', '',regex = False)
    s = s = s.replace({'-': np.nan, '—': np.nan, '': np.nan}).astype(object)
    return pd.to_numeric(s, errors='coerce')
price_col =  ['12m Low','12m High','Day Low','Day High','Day Price','Previous','Change','Change%','Volume','Adjusted Price']
for c in price_col:
    if c in df.columns:
        df[c + '_num'] = clean_numeric_series(df[c], percent=(c=='Change%'))
#Dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Date'].isnull().sum()
#saving onto a new file
df.to_csv('nse_cleaned.csv', index = False)
cleaned_df = pd.read_csv('nse_cleaned.csv')
cleaned_df.head()
cleaned_df.describe().T
cleaned_df.columns
#keeping 0nly num cols
id_cols = ['Date', 'Code', 'Name']
num_cols = [c for c in df.columns if c.endswith('_num')]
df_numeric_only = df[id_cols + num_cols]
df_numeric_only.to_csv("nse_numeric_only.csv", index=False)
