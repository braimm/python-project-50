def make_sp(value):
    return value * ' '


def value_to_string(value, shift):
    result = ''
    if isinstance(value, dict):
        result += '{\n'
        shift += 4
        sp = make_sp(shift)
        for i in value:
            result += f"{sp}  {i}: {value_to_string(value[i], shift)}\n"
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

    shift += 4
    for node in diff:
        name_node = f"{node['key']}"
        value_1 = node.get('value_1')
        value_2 = node.get('value_2')
        sp = make_sp(shift)
        if node['status_tag'] == 'only_data_1':
            result += f"{sp}- {name_node}: {value_to_string(value_1, shift)}\n"
        elif node['status_tag'] == 'only_data_2':
            result += f"{sp}+ {name_node}: {value_to_string(value_1, shift)}\n"
        elif node['status_tag'] == 'non_changed':
            result += f"{sp}  {name_node}: {value_to_string(value_1, shift)}\n"
        elif node['status_tag'] == 'changed':
            result += f"{sp}- {name_node}: {value_to_string(value_1, shift)}\n"
            result += f"{sp}+ {name_node}: {value_to_string(value_2, shift)}\n"
        else:
            result += f"{sp}  {name_node}: {stylish(node['nested'], shift)}\n"

    result += f"{make_sp(shift - 2)}" + "}"
    return result
