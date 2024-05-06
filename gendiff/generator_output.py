


def generate_output_old(data_file1, data_file2, diff):    
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

def make_sp(value):
    return value * ' '



def value_to_string(value, shift):
    result = ''
    if isinstance(value, dict):
        result += '{\n'
        shift += 4
        for i in value:
            result += f"{make_sp(shift)}  {i}: {value_to_string(value[i], shift)}\n"
        result += f"{make_sp(shift - 2)}" + "}"    
    elif value is None:
        result += 'null'
    elif value in [True, False]:
        result += str(value).lower()
    else:
        result += str(value)
    return result


def stylish(diff, shift=-2):
    result = '{\n'
    #"""
    shift += 4
    for node in diff:
        if node['status_tag'] == 'only_data_1':
            result += f"{make_sp(shift)}- {node['key']}: {value_to_string(node['value'], shift)}\n"
        elif node['status_tag'] == 'only_data_2':
            result += f"{make_sp(shift)}+ {node['key']}: {value_to_string(node['value'], shift)}\n"
        elif node['status_tag'] == 'non_changed':
            result += f"{make_sp(shift)}  {node['key']}: {value_to_string(node['value'], shift)}\n"
        elif node['status_tag'] == 'changed':
            result += f"{make_sp(shift)}- {node['key']}: {value_to_string(node['value_1'], shift)}\n"
            result += f"{make_sp(shift)}+ {node['key']}: {value_to_string(node['value_2'], shift)}\n"            
        else:
            result += f"{make_sp(shift)}  {node['key']}: {stylish(node['nested'], shift)}\n"
    #"""
    result += f"{make_sp(shift - 2)}" + "}"
    return result

def generate_output(diff, format='stylish'):
    if format == 'stylish':
        oputput = stylish(diff)
    return oputput