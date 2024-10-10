import json
from scrapper import extract_all_li_text

def lambda_handler(event, context):
    # TODO implement
    values = extract_all_li_text()
    return {
        'response': values # list of strings
    }
