import pandas as pd 

def data_preprocess_normalize(df: pd.DataFrame) -> pd.DataFrame:
    # Calculate the average price
    df['average'] = (df['Open'] + df['High'] + df['Low']) / 3
    
    # Calculate min and max of the 'average' column
    min_val = df['average'].min()
    max_val = df['average'].max()
    
    # Normalize the average price using min-max normalization
    df['normalized_average'] = (df['average'] - min_val) / (max_val - min_val)
    
    return df
