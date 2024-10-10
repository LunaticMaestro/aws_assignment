import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def data_create_model(df: pd.DataFrame):
    trend_slopes = {}  # Dictionary to store the slope of each ticker's trend line

    # Group by 'ticker' and calculate the trend line slope for each group
    for ticker, group in df.groupby('ticker'):
        # Reset index to ensure sequential data points for the trend calculation
        group = group.reset_index()
        
        # Independent variable (x): index (day count)
        x = group.index.to_numpy()
        # Dependent variable (y): normalized average values
        y = group['normalized_average'].to_numpy()
        
        # Fit a linear regression (trend line) to find the slope
        slope, intercept = np.polyfit(x, y, 1)  # 1 represents a linear fit (y = mx + c)
        
        # Store the slope in the dictionary with the ticker name as key
        trend_slopes[ticker] = float(slope)

    # Identify the ticker with the greatest trend line slope
    best_performer = max(trend_slopes, key=trend_slopes.get)
    print(f"Best performing ticker: {best_performer} with a slope of {trend_slopes[best_performer]}")

    # Plot the trend lines for each ticker
    plt.figure(figsize=(10, 6))
    for ticker, group in df.groupby('ticker'):
        group = group.reset_index()
        x = group.index.to_numpy()
        y = group['normalized_average'].to_numpy()
        
        # Plot the normalized averages as a line plot
        plt.plot(x, y, label=f"{ticker} (slope: {trend_slopes[ticker]:.2f})")

        # Plot the trend line
        trend_line = trend_slopes[ticker] * x + intercept  # Use slope and intercept from polyfit
        plt.plot(x, trend_line, linestyle='dashed')

    # Adding titles and labels
    plt.title("Trend Lines of Normalized Averages for Each Ticker")
    plt.xlabel("Days")
    plt.ylabel("Normalized Average")
    plt.legend()
    plt.grid(True)

    # Save the plot to a BytesIO buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Close the figure to prevent it from displaying

    # Encode the image as base64
    buffer.seek(0)
    img_bytes = buffer.read()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    
    return trend_slopes, best_performer, img_base64
