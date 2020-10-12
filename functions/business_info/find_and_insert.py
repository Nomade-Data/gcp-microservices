import requests
import json
import datetime
from google.cloud import bigquery

def find_and_insert(_key):
    r = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(str(_key).zfill(14)))
    
    rd = json.loads(r.text)
    
    if rd['atividade_principal'][0]['code'][:2] not in ['55']:
        return [{'error': 'cnpj nao corresponde ao grupo de alojamento'}]

    if 'cnpj' in rd:
        cnpj = rd['cnpj']
        atividade_principal_code = rd['atividade_principal'][0]['code']
        atividade_principal_text = rd['atividade_principal'][0]['text']
        cep = rd['cep']
        uf = rd['uf']
        municipio = rd['municipio']
        fantasia = rd['fantasia']
        nome = rd['nome']
        natureza_juridica = rd['natureza_juridica']
        situacao = rd['situacao']
        ultima_atualizacao = rd['ultima_atualizacao']
        
        row1 = {
            "id": _key,
            "cnpj": cnpj,
            "atividade_principal_code": atividade_principal_code,
            "atividade_principal_text": atividade_principal_text,
            "cep": cep,
            "uf": uf,
            "municipio": municipio,
            "fantasia": fantasia,
            "nome": nome,
            "natureza_juridica": natureza_juridica,
            "situacao": situacao,
            "ultima_atualizacao": ultima_atualizacao,
            "insert_datetime": datetime.datetime.now().isoformat(),
        }
        rows_to_insert = [row1]
        
        client = bigquery.Client()
        
        errors = client.insert_rows_json('hackgetnet-team56.raw.receita_federal_cnpj', rows_to_insert)
        
        if errors == []:
            print("New cnpj have been added on receita_federal_cnpj ({}).".format(_key))
        else:
            raise ValueError(errors)
            
        return [{k: v for k, v in row1.items() if k in ['id', 'nome', 'municipio', 'uf'] }]
    else:
        raise ValueError("CNPJ nao encontrado na receita federal")
