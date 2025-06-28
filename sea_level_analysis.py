
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load dataset
df = pd.read_csv("epa-sea-level.csv")

# Plot function
def draw_sea_level_plot():
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, label='Data')

    # Linear regression for all years
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    plt.plot(x_all, y_all, 'r', label='Fit: All Data')

    # Linear regression from year 2000
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_2000.slope * x_recent + res_2000.intercept
    plt.plot(x_recent, y_recent, 'g', label='Fit: 2000–2013')

    # Formatting
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    return plt.gcf()

# Run the plot
if __name__ == "__main__":
    draw_sea_level_plot()
    plt.show()
