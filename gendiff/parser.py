import json
import yaml
from yaml.loader import SafeLoader


def get_data_file(path):
    file = open(path)
    data = file.read()
    file.close()
    return data


def get_type_file(path):
    YAML = ("yaml", "yml")
    type_file = path.split('.')
    type_file = type_file[len(type_file) - 1]
    if type_file in YAML:
        return "yml"
    return 'json'


def get_parsed_data(path):
    data = get_data_file(path)
    type_file = get_type_file(path)
    if type_file == "json":
        return json.loads(data)
    return yaml.load(data, Loader=SafeLoader)
