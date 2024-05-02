import os
import json

def generate_diff(path1, path2):
    file1 = open(path1)
    file2 = open(path2)
    data_file1 = json.loads(file1.read())
    data_file2 = json.loads(file2.read())
    print(data_file1)
    print(data_file2)
    diff_file1 = []
    diff_file2 = []
    share = []
    
    for key_from_file1, value_from_file1 in data_file1.items():
        if data_file2.get(key_from_file1):
            value_from_file2 = data_file2[key_from_file1]
            if value_from_file1 == value_from_file2:
                share.append(key_from_file1)
            else:
                diff_file1.append(key_from_file1)
                diff_file2.append(key_from_file1)
        else:
            diff_file1.append(key_from_file1)
    
    list_viewed_keys = diff_file1 + share
    
    
    for key_from_file2 in data_file2:
        if key_from_file2 not in list_viewed_keys:
            diff_file2.append(key_from_file2)

    list_viewed_keys += diff_file2
    
    list_viewed_keys = sorted(list(set(list_viewed_keys)))
    print()
    print()
    print(diff_file1)
    print(diff_file2)
    print(share)
    print()
    print(list_viewed_keys)


    result = '{\n'
    for key in list_viewed_keys:
        if key in diff_file1 and key in diff_file2:
            result += f"  - {key}: {str(data_file1[key]).lower()}\n"
            result += f"  + {key}: {str(data_file2[key]).lower()}\n"
        elif key in diff_file1 and key not in diff_file2:
            result += f"  - {key}: {str(data_file1[key]).lower()}\n"
        elif key in diff_file2 and key not in diff_file1:
            result += f"  + {key}: {str(data_file2[key]).lower()}\n"
        else:
            result += f"    {key}: {str(data_file2[key]).lower()}\n"

    result += '}'
    return result
    