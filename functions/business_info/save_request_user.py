import datetime
from google.cloud import bigquery

def save_request_user(_user, _key):
    
    rows_to_insert = [
        {
            "id": _key,
            "user": _user,
            "insert_datetime": datetime.datetime.now().isoformat(),
        },
    ]
    
    client = bigquery.Client()
    
    errors = client.insert_rows_json('hackgetnet-team56.raw.request_user', rows_to_insert)
    
    if errors == []:
        print("New rows have been added on request_user ({}, {}).".format(_user, _key))
    else:
        raise ValueError(errors)
