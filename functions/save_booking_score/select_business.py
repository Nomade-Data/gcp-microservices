from google.cloud import bigquery

def select_business(_key):
    client = bigquery.Client()

    result = client.query('select id, score, localizationScore from hackgetnet-team56.raw.booking_score where id = {}'.format(_key))

    return result.result()