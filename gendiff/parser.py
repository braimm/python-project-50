import os
import json
import yaml
from yaml.loader import SafeLoader

SUPPORT_TYPE = ("yaml", "yml", "json")


def get_data_file(path):
    with open(path, "r") as file:
        data = file.read()
    return data


def get_format_name(path):
    data_format = os.path.splitext(path)[1][1:]
    if data_format in SUPPORT_TYPE:
        return data_format
    raise ValueError(f"Unsupported format file: {data_format}")


def parse(data, data_format):
    match data_format:
        case "json":
            return json.loads(data)
        case 'yml':
            return yaml.load(data, Loader=SafeLoader)
        case 'yaml':
            return yaml.load(data, Loader=SafeLoader)


def get_parsed_data(path):
    data = get_data_file(path)
    data_format = get_format_name(path)
    return parse(data, data_format)
