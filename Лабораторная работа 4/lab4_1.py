# TODO решите задачу
import json


def task() -> float:
    with open("input.json", 'r') as f:
        file_json = json.load(f)
        proizv = [object['score'] * object['weight'] for object in file_json]
    return round(sum(proizv), 3)


print(task())
