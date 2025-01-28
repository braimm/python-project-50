def get_formatted_value(value):
    result = ''
    if isinstance(value, dict):
        result = "[complex value]"
    elif value is None:
        result += "null"
    elif value in [True, False]:
        result += str(value).lower()
    else:
        result += f"'{value}'"
    return result


def plain(diff, name_node_parrent=''):
    result = ''
    for node in diff:
        name_node = f"{node['key']}"
        value_1 = node.get('value_1')
        value_2 = node.get('value_2')
        tag = node['status_tag']

        match tag:
            case 'only_data_1':
                result += (f"Property '{name_node_parrent}{name_node}' "
                           f"was removed\n")

            case 'only_data_2':
                result += (f"Property '{name_node_parrent}{name_node}' "
                           f"was added with value: "
                           f"{get_formatted_value(value_1)}\n")

            case 'changed':
                result += (f"Property '{name_node_parrent}{name_node}' "
                           f"was updated. "
                           f"From {get_formatted_value(value_1)} to "
                           f"{get_formatted_value(value_2)}\n")

            case 'nested':
                name_node = f'{name_node_parrent}{name_node}.'
                result += plain(node['nested'], name_node)

    return result
