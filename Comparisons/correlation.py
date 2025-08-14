import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv(r"nse_numeric_only.csv")

# Keep only Date, Code, and Price
df_pivot = df.pivot(index="Date", columns="Code", values="Day Price_num")

# Calculate daily returns
returns = df_pivot.pct_change()

# Get correlation matrix
corr_matrix = returns.corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(
    corr_matrix,
    annot=False,             # Remove numbers from the cells
    cmap="coolwarm",          # Color gradient from cool (negative) to warm (positive)
    center=0,                 # Center the colormap at 0
    linewidths=0.5,           # Add small gaps between squares
    square=True,              # Make cells square-shaped
    cbar_kws={'shrink': 0.75} # Smaller color bar
)
plt.title("Stock Price Correlation Heatmap", fontsize=16)
plt.show()

