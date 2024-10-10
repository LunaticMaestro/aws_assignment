import json
import boto3
import pandas as pd
from io import StringIO


def lambda_handler(event, context):
    # Create a sample pandas DataFrame
    
    
    # AWS S3 client
    s3 = boto3.client('s3')
    
    # Bucket name and file name
    bucket_name = 'z-ec-bucket-data'
    
    # Process each incoming ticker 
    for ticker_data in event['response']:
        for ticker, data in ticker_data.items(): # only one k,v is there in each
                
            # parse data
            df = pd.read_json(StringIO(data))
            print("--", df.columns)
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False) 

            file_name = f'stock_{ticker}.csv'
            
            # Upload CSV to S3
            try:
                s3.put_object(
                    Bucket=bucket_name, 
                    Key=file_name, 
                    Body=csv_buffer.getvalue()
                )
                print(f'stock_{ticker}.csv stored in {bucket_name}')
                
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps(f"Error storing file in S3: {str(e)}")
                }
    return {
        'statusCode': 200,
        'body': json.dumps('CSV file stored successfully in S3')
    }
