import pandas as pd
import matplotlib.pyplot as plt

class StockAnalyzer:
    def __init__(self, csv_path):
        """Initialize with CSV file path"""
        self.df = pd.read_csv(csv_path)
        self.preprocess()
        self.grouped = self.group_by_code()

    def preprocess(self):
        """Convert numeric fields and clean data"""
        numeric_cols = ['Day Price_num', 'Change%_num', 'Volume_num']
        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        self.df.dropna(subset=['Code'], inplace=True)

    def group_by_code(self):
        """Aggregate by stock code"""
        grouped = self.df.groupby('Code').agg({
            'Name': 'first',
            'Day Price_num': 'mean',
            'Change%_num': 'mean',
            'Volume_num': 'mean'
        }).reset_index()
        return grouped
    def compare_stocks(self, codes):
        """Compare selected stocks via bar charts"""
        codes = [c.strip().upper() for c in codes]
        compare_df = self.grouped[self.grouped['Code'].isin(codes)]
        if compare_df.empty:
            print("No matching stock codes found.")
            return

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        axes[0].bar(compare_df['Code'], compare_df['Day Price_num'], color='skyblue')
        axes[0].set_title('Avg Price'); axes[0].set_ylabel('Price')

        axes[1].bar(compare_df['Code'], compare_df['Change%_num'], color='orange')
        axes[1].set_title('Avg % Change'); axes[1].set_ylabel('% Change')

        axes[2].bar(compare_df['Code'], compare_df['Volume_num'], color='green')
        axes[2].set_title('Avg Volume'); axes[2].set_ylabel('Volume')

        plt.suptitle(f"Comparison: {', '.join(codes)}", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def trend_comparison(self, codes):
        """Plot historical price trends for selected stocks"""
        codes = [c.strip().upper() for c in codes]
        plt.figure(figsize=(10, 6))
        for code in codes:
            stock_data = self.df[self.df['Code'] == code]
            if stock_data.empty:
                print(f"No data for {code}")
                continue
            plt.plot(stock_data.index, stock_data['Day Price_num'], label=code)
        plt.xlabel('Record Index')
        plt.ylabel('Price')
        plt.title('Price Trends Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    analyzer = StockAnalyzer(
        r"C:\Users\gh\Desktop\Nairobi Securities Exchange\By Stock\nse_numeric_only.csv"
    )

    codes_input = input("\nEnter stock codes to compare (comma-separated): ").split(",")
    analyzer.compare_stocks(codes_input)

    

    analyzer.trend_comparison(codes_input)
    print(  "Analysis complete. Check the plots for results.") 