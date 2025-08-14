
import pandas as pd
import matplotlib.pyplot as plt

def plot_two_stock_correlation(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Pivot so each stock code is a column
    df_pivot = df.pivot(index="Date", columns="Code", values="Day Price_num")

    # Ask user for stock codes
    stock1 = input("Enter first stock code: ").strip().upper()
    stock2 = input("Enter second stock code: ").strip().upper()

    # Check if they exist in dataset
    if stock1 not in df_pivot.columns or stock2 not in df_pivot.columns:
        print("One or both stock codes not found in dataset.")
        print("Available codes:", list(df_pivot.columns))
        return

    # Drop missing values for both stocks
    data = df_pivot[[stock1, stock2]].dropna()

    # Calculate correlation
    correlation = data[stock1].corr(data[stock2])
    print(f"\nCorrelation between {stock1} and {stock2}: {correlation:.2f}")

    # Plot scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(data[stock1], data[stock2], alpha=0.7, edgecolors='w', s=80)
    plt.title(f"Price Correlation: {stock1} vs {stock2}\nCorrelation = {correlation:.2f}")
    plt.xlabel(f"{stock1} Price")
    plt.ylabel(f"{stock2} Price")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

if __name__ == "__main__":
    # Change this to your CSV path
    plot_two_stock_correlation(r"C:\Users\gh\Desktop\Nairobi Securities Exchange\nse_numeric_only.csv")
 