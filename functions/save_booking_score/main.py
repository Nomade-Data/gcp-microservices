import json
from select_business import select_business
from check_if_exist import check_if_exist
from insert_booking_score import insert_booking_score

def reload(request):
    request_json = request.get_json()

    key = request_json['key']
    name = request_json['name']
    city = request_json['city']

    if check_if_exist(key) == 0:
        result = insert_booking_score(key, name, city)
    else:
        result = select_business(key)
        
    records = [dict(row) for row in result]
    json_obj = json.dumps(records)

    return json_obj