import json
import random

def reload(request):
    request_json = request.get_json()

    key = request_json['id']
    value = request_json['value']

    n = random.randint(1, 999)
    result = [{'score': n}]
        
    json_obj = json.dumps(result)

    return json_obj