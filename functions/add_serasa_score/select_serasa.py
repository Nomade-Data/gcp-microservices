from google.cloud import bigquery

def select_serasa(_key):
    client = bigquery.Client()

    result = client.query('select id, score, detalhe, valor_divida from hackgetnet-team56.raw.serasa_score where id = {}'.format(_key))
    
    return result.result()