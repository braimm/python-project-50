# import os
from gendiff.parser import get_parsed_data


def generate_output(data_file1, data_file2, diff):    
    keys_only_data_1, keys_only_data_2, keys_share = diff
    all_keys = set(keys_only_data_1 + keys_only_data_2 + keys_share)
    all_keys = sorted(list(all_keys))

    result = '{\n'
    for key in all_keys:
        if key in keys_only_data_1 and key in keys_only_data_2:
            result += f"  - {key}: {str(data_file1[key]).lower()}\n"
            result += f"  + {key}: {str(data_file2[key]).lower()}\n"
        elif key in keys_only_data_1:
            result += f"  - {key}: {str(data_file1[key]).lower()}\n"
        elif key in keys_only_data_2:
            result += f"  + {key}: {str(data_file2[key]).lower()}\n"
        else:
            result += f"    {key}: {str(data_file2[key]).lower()}\n"
    result += '}'
    return result


def get_diff(data_1, data_2):
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


def generate_diff(path_1, path_2):
    data_file1 = get_parsed_data(path_1)
    data_file2 = get_parsed_data(path_2)
    print(data_file1)
    print(data_file2)
    diff = get_diff(data_file1, data_file2)
    output = generate_output(data_file1, data_file2, diff)
    return output