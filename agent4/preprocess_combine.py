import pandas as pd

def data_preprocess_combine(data: dict) -> pd.DataFrame:
    # Initialize an empty list to store individual DataFrames with ticker information
    frames = []
    
    # Iterate through each ticker and its associated DataFrame in the dictionary
    for ticker, df in data.items():
        # Add a new column 'ticker' with the name of the stock ticker
        df = df.copy()  # Avoid modifying the original DataFrame
        df['ticker'] = ticker
        
        # Append the modified DataFrame to the list
        frames.append(df)
        
    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(frames, ignore_index=True)
    
    return combined_df
