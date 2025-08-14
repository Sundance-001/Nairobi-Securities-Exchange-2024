import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\gh\Desktop\stocks\stocks.csv")
#df['Date'] = pd.to_datetime(df['Date'])
#df.set_index('Date', inplace=True)
#df['Close'].plot(title='Stock Closing Prices')
plt.ylabel('Price ($)')
plt.grid(True)
plt.show()

