import json
import boto3
import os
import csv
from io import StringIO
import pandas as pd

# Initialize the S3 client
s3_client = boto3.client('s3')

def read_s3():
    global s3_client
    # # Get the S3 bucket name from environment variable
    # bucket_name = os.environ.get('BUCKET_NAME')
    bucket_name = "z-ec-bucket-data"
    
    # Initialize an empty list to store the CSV contents
    df_dict = {}

    try:
        # List objects in the specified S3 bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # Check if any contents were found
        if 'Contents' in response:
            for obj in response['Contents']:
                object_key = obj['Key']
                
                # Check if the object key matches the pattern 'stock_*.csv'
                if object_key.startswith('stock_') and object_key.endswith('.csv'):
                    # Get the object
                    ticker = str(object_key).lstrip("stock_").rstrip(".csv")
                    
                    try:
                        csv_obj = s3_client.get_object(Bucket=bucket_name, Key=object_key)
                        body = csv_obj['Body'].read().decode('utf-8')
                        # Read the CSV content into a DataFrame directly
                        df = pd.read_csv(StringIO(body))
                        df_dict[ticker] = df
                        
                    except Exception as e:
                        print("error reading ticker: ", object_key)
                    
    except Exception as e:
        print(f"error: {e}")
        
    return df_dict
