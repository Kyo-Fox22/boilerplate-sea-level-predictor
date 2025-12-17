import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m, b = res.slope, res.intercept
    func = lambda x: m*x + b
    
    plt.plot(range(1880,2051), [func(x) for x in range(1880, 2051)])
    
    # Create second line of best fit
    new_df = df[['Year','CSIRO Adjusted Sea Level']].set_index('Year').loc[2000:,:].copy()
    res2 = linregress(new_df.index, new_df['CSIRO Adjusted Sea Level'])
    m2, b2 = res2.slope, res2.intercept
    func2 = lambda x: m2*x + b2

    plt.plot(range(2000,2051), [func2(x) for x in range(2000, 2051)])

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()