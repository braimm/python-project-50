import json


def to_json(diff):
    return json.dumps(diff, indent=4, separators=(',', ': '))
