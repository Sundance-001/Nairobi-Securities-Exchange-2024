import matplotlib.pyplot as plt
from daily_statistics import*

# # # Bar chart: prices
plt.figure(figsize=(10,5))
plt.bar(df_on_date['Code'], df_on_date['Day Price_num'])
plt.xticks(rotation=90)
plt.ylabel("Day Price")
plt.title(f"Stock Prices on {target_date.date()}")
plt.tight_layout()
plt.show()

# Bar chart: % change
plt.figure(figsize=(10,5))
plt.bar(df_on_date['Code'], df_on_date['Change%_num'])
plt.xticks(rotation=90)
plt.ylabel("Change %")
plt.title(f"Price Change % on {target_date.date()}")
plt.axhline(0, color='red', linestyle='--')
plt.tight_layout()
plt.show()
