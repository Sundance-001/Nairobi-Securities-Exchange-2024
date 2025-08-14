from Choosing_date import*
df_on_date.head()
df_on_date.describe()
highest_stock = df_on_date.loc[df_on_date['Day Price_num'].idxmax()]
print("Highest Price Stock:\n", highest_stock)
lowest_stock = df_on_date.loc[df_on_date['Day Price_num'].idxmin()]
print("Lowest Price Stock:\n", lowest_stock)
total_volume = df_on_date['Volume_num'].sum()
most_traded = df_on_date.loc[df_on_date['Volume_num'].idxmax()]
print(f"Total Volume: {total_volume:,}")
print("Most Traded Stock:\n", most_traded)
avg_change = df_on_date['Change%_num'].mean()
print(f"Average % Change: {avg_change:.2f}%")
top_gainers = df_on_date.sort_values('Change%_num', ascending=False).head(5)
top_losers = df_on_date.sort_values('Change%_num', ascending=True).head(5)
print("Top Gainers:\n", top_gainers[['Code', 'Change%_num']])
print("Top Losers:\n", top_losers[['Code', 'Change%_num']])

