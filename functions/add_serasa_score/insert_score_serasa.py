import datetime
from google.cloud import bigquery

def insert_score_serasa(_request_json):
    row1 = {
        "id": _request_json['id'],
        "score": _request_json['score'],
        "detalhe": _request_json['detalhe'],
        "valor_divida": _request_json['valor_divida'],
        "insert_datetime": datetime.datetime.now().isoformat(),   
    }
    rows_to_insert = [row1]
    
    client = bigquery.Client()
    
    errors = client.insert_rows_json('hackgetnet-team56.raw.serasa_score', rows_to_insert)
    
    if errors == []:
        print("New rows have been added on request_user ({}).".format(_request_json['id']))
    else:
        raise ValueError(errors)
    
    return [{k: v for k, v in row1.items() if k in ['id', 'score', 'detalhe', 'valor_divida'] }]
