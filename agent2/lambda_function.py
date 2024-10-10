import json
from stock import get_3m_data, to_json

def lambda_handler(event, context):
    # TODO implement
    data = []
    for ticker in event['response']:
        df = get_3m_data(ticker)
        json_response = to_json(df, ticker)
        data.append(json_response) 
        
    return {
        'response': data
    }
