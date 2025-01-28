import json
import yaml
from yaml.loader import SafeLoader


def get_data_file(path):
    with open(path, "r") as file:
        data = file.read()
    return data


def get_type_file(path):
    SUPPORT_TYPE = ("yaml", "yml", "json")
    type_file = path.split('.')
    type_file = type_file[len(type_file) - 1]
    if type_file in SUPPORT_TYPE:
        return type_file
    raise ValueError(f"Unsupported format file: {type_file}")


def get_parsed_data(path):
    data = get_data_file(path)
    type_file = get_type_file(path)
    match type_file:
        case "json":
            return json.loads(data)
        case 'yml':
            return yaml.load(data, Loader=SafeLoader)
        case 'yaml':
            return yaml.load(data, Loader=SafeLoader)
