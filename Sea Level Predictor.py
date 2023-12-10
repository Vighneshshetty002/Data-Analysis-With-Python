import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read sea level data into a DataFrame (replace 'your_data.csv' with your actual data file)
    df = pd.read_csv('your_data.csv')

    # Create a linear regression model
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Generate predictions for future years
    future_years = np.arange(df['Year'].min(), 2051, 1)
    future_levels = slope * future_years + intercept

    # Plot the original data
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Plot the linear regression line
    plt.plot(future_years, future_levels, color='red', label='Linear Regression')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_plot.png')
    plt.show()

# Example usage
draw_plot()
