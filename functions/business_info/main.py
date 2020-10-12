import json
from select_business import select_business
from check_if_exist import check_if_exist
from save_request_user import save_request_user
from find_and_insert import find_and_insert

def reload(request):
    request_json = request.get_json()

    user = request_json['user']
    key = request_json['key']

    save_request_user(user, key)

    if check_if_exist(key) == 0:
        result = find_and_insert(key)
    else:
        result = select_business(key)
        
    records = [dict(row) for row in result]
    json_obj = json.dumps(records)

    return json_obj