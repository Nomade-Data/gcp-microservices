from google.cloud import bigquery

def check_if_exist(_key):
    client = bigquery.Client()

    result = client.query('select id from hackgetnet-team56.raw.booking_score where id = {}'.format(_key))

    return result.result().total_rows