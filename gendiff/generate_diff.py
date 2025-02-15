from gendiff.parser import get_parsed_data
from gendiff.formatters import generate_output


def get_diff(data_1, data_2):
    all_keys = set(data_1.keys()) | set(data_2.keys())

    diff = []
    all_keys = sorted(list(all_keys))

    for key in all_keys:
        value_1 = data_1.get(key)
        value_2 = data_2.get(key)
        if key in data_1.keys() and key not in data_2.keys():
            diff.append(
                {"key": key,
                 "value_1": value_1,
                 "status_tag": "only_data_1"})

        elif key in data_2.keys() and key not in data_1.keys():
            diff.append(
                {"key": key,
                 "value_1": value_2,
                 "status_tag": "only_data_2"})

        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            diff.append(
                {"key": key,
                 "nested": get_diff(value_1, value_2),
                 "status_tag": "nested"})

        elif value_1 != value_2:
            diff.append(
                {"key": key,
                 "value_1": value_1,
                 "value_2": value_2,
                 "status_tag": "changed"})

        else:
            diff.append(
                {"key": key, "value_1": value_2, "status_tag": "non_changed"})
    return diff


def generate_diff(path_1, path_2, format='stylish'):
    data_file1 = get_parsed_data(path_1)
    data_file2 = get_parsed_data(path_2)
    diff = get_diff(data_file1, data_file2)
    formatted_output = generate_output(diff, format)
    return formatted_output
