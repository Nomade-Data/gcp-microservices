from google.cloud import bigquery

def select_business(_key):
    client = bigquery.Client()

    result = client.query('select id, nome, municipio, uf from hackgetnet-team56.raw.receita_federal_cnpj where id = {}'.format(_key))

    return result.result()