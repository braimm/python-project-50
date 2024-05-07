# import os
from gendiff.parser import get_parsed_data
from gendiff.formatters.generator_output import generate_output


def get_sets_keys(data_1, data_2):
    keys_only_data_1 = set()
    keys_only_data_2 = set()
    viewed_keys = set()
    for key_data_1 in data_1.keys():
        if key_data_1 not in data_2.keys():
            keys_only_data_1.add(key_data_1)
            viewed_keys.add(key_data_1)
        else:
            viewed_keys.add(key_data_1)

    for key_data_2 in data_2.keys():
        if key_data_2 not in data_1.keys():
            keys_only_data_2.add(key_data_2)
            viewed_keys.add(key_data_2)
        else:
            viewed_keys.add(key_data_2)

    return viewed_keys, keys_only_data_1, keys_only_data_2


def get_diff(data_1, data_2):
    all_keys, \
        keys_only_data_1, \
        keys_only_data_2 \
        = get_sets_keys(data_1, data_2)

    diff = []
    all_keys = sorted(list(all_keys))

    for key in all_keys:
        value_1 = data_1.get(key)
        value_2 = data_2.get(key)
        if key in keys_only_data_1:

            diff.append(
                {"key": key,
                 "value_1": value_1,
                 "status_tag": "only_data_1"})
        elif key in keys_only_data_2:

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
    # print(diff)
    formatted_output = generate_output(diff, format)
    return formatted_output
