# import os
from gendiff.parser import get_parsed_data
from gendiff.generator_output import generate_output

def get_diff_old(data_1, data_2):
    keys_only_data_1 = []
    keys_only_data_2 = []
    keys_share = []

    for key_data_1, value_data_1 in data_1.items():
        if data_2.get(key_data_1):
            value_data_2 = data_2[key_data_1]
            if value_data_1 == value_data_2:
                keys_share.append(key_data_1)
            else:
                keys_only_data_1.append(key_data_1)
                keys_only_data_2.append(key_data_1)
        else:
            keys_only_data_1.append(key_data_1)

    list_viewed_keys = keys_only_data_1 + keys_share

    for key_data_2 in data_2:
        if key_data_2 not in list_viewed_keys:
            keys_only_data_2.append(key_data_2)
    print()
    print()
    print(keys_only_data_1)
    print(keys_only_data_2)
    print(keys_share)
    print()
    print(list_viewed_keys)
    print()
    return keys_only_data_1, keys_only_data_2, keys_share
    #list_viewed_keys += keys_only_data_2


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
    """ Удалить после завершение
    print()                                         
    print()
    print(keys_only_data_1)
    print(keys_only_data_2)
    print()
    print(viewed_keys)
    print()
    """
    return viewed_keys, keys_only_data_1, keys_only_data_2


def get_diff(data_1, data_2):
    all_keys, keys_only_data_1, keys_only_data_2  = get_sets_keys(data_1, data_2)
    diff = []
    all_keys = sorted(list(all_keys))

    for key in all_keys:
        value_1 = data_1.get(key)
        value_2 = data_2.get(key)
        if key in keys_only_data_1:

            diff.append({"key": key, "value": value_1, "status_tag": "only_data_1"})
        elif key in keys_only_data_2:

            diff.append({"key": key, "value": value_2, "status_tag": "only_data_2"})
        elif isinstance(value_1, dict) and isinstance(value_2, dict):

            diff.append({"key": key, "nested": get_diff(value_1, value_2), "status_tag": "nested"})
        elif value_1 != value_2:

            diff.append({"key": key, "value_1": value_1, "value_2": value_2, "status_tag": "changed"})
        else:

            diff.append({"key": key, "value": value_2, "status_tag": "non_changed"})
    return diff


def generate_diff(path_1, path_2):
    data_file1 = get_parsed_data(path_1)
    data_file2 = get_parsed_data(path_2)
    diff = get_diff(data_file1, data_file2)
    return diff