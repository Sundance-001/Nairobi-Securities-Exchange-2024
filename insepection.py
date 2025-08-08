
#initial inspection
import pandas as pd
df = pd.read_csv(r"C:\Users\gh\Desktop\NSE_data_all_stocks_2024_jan_to_oct.csv")
df.head()
df[200:210]
df.info()
df.T
df.describe(include = 'all').transpose()
