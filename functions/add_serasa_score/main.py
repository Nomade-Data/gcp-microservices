import json
from check_if_exist import check_if_exist
from insert_score_serasa import insert_score_serasa
from select_serasa import select_serasa


def reload(request):
    request_json = request.get_json()

    if check_if_exist(request_json['id']) == 0:
        result = insert_score_serasa(request_json)
    else:
        result = select_serasa(request_json['id'])
        
    records = [dict(row) for row in result]
    json_obj = json.dumps(records)

    return json_obj