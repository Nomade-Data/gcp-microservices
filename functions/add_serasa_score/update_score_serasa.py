from google.cloud import bigquery
from create_update import create_update

def update_score_serasa(_request_json):
    client = bigquery.Client()
    
    qy = create_update('raw.serasa_score', ["score", "detalhe", "valor_divida"], _request_json, True)

    query_job = client.query(qy)
    
    query_job.result()