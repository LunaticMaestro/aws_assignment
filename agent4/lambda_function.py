import json

from load_s3_data import read_s3
from preprocess_combine import data_preprocess_combine
from preprocess_normalize import data_preprocess_normalize
from best_performer import data_create_model

def lambda_handler(event, context):
    # TODO implement
    df_dict = read_s3()
    df = data_preprocess_combine(df_dict)
    df = data_preprocess_normalize(df)
    trends, best_performer, viz = data_create_model(df)
    # print(best_performer)
    # print(trends)
    
    return {
        'best_performer': best_performer,
        'trends': trends,
        'viz': viz
    }
