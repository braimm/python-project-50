import json
import yaml
from yaml.loader import SafeLoader


def get_data_file(path):
    # file = open(path)
    # data = file.read()
    # file.close()
    with open(path, "r") as file:
        data = file.read()
    return data


def get_type_file(path):
    YAML = ("yaml", "yml")
    type_file = path.split('.')
    type_file = type_file[len(type_file) - 1]
    return "yml" if type_file in YAML else "json"


def get_parsed_data(path):
    data = get_data_file(path)
    type_file = get_type_file(path)
    match type_file:
        case "json":
            return json.loads(data)
        case 'yml':
            return yaml.load(data, Loader=SafeLoader)
