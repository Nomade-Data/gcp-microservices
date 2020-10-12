import requests
import json
import datetime
from google.cloud import bigquery

def insert_booking_score(_key, _name, _city):

    #request
    mydata = {
        "name": _name,
        "city": _city
    }

    response = requests.post('https://us-central1-hackgetnet-team56.cloudfunctions.net/crawler_booking', data=mydata)
    
    request_json = response.json()
    score = request_json['score']
    localizationScore = request_json['localizationScore']

    row1 = {
        "id": _key,
        "score": score,
        "localizationScore": localizationScore,
        "insert_datetime": datetime.datetime.now().isoformat(),
    }
    rows_to_insert = [row1]
    
    client = bigquery.Client()
    
    errors = client.insert_rows_json('hackgetnet-team56.raw.booking_score', rows_to_insert)
    
    if errors == []:
        print("New cnpj have been added on booking_score ({}).".format(_key))
    else:
        raise ValueError(errors)
        
    return [{k: v for k, v in row1.items() if k in ['id', 'score', 'localizationScore'] }]
