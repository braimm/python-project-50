def make_ident(value):
    return (value * 4 - 2) * ' '


def make_ident_bracket(value):
    return (value * 4 - 4) * ' '


def value_to_string(value, level):
    result = ''
    if isinstance(value, dict):
        level += 1
        result += '{\n'
        ident = make_ident(level)
        ident_bracket = make_ident_bracket(level)
        for i in value:
            result += f"{ident}  {i}: {value_to_string(value[i], level)}\n"
        result += f"{ident_bracket}" + "}"
    elif value is None:
        result += 'null'
    elif value in [True, False]:
        result += str(value).lower()
    else:
        result += str(value)
    return result


def stylish(diff, level=0):
    result = '{\n'
    level += 1

    for node in diff:
        name_node = f"{node['key']}"
        value_1 = node.get('value_1')
        value_2 = node.get('value_2')
        ident = make_ident(level)
        ident_bracket = make_ident_bracket(level)

        if node['status_tag'] == 'only_data_1':
            result += (f"{ident}- {name_node}: "
                       f"{value_to_string(value_1, level)}\n")

        elif node['status_tag'] == 'only_data_2':
            result += (f"{ident}+ {name_node}: "
                       f"{value_to_string(value_1, level)}\n")

        elif node['status_tag'] == 'non_changed':
            result += (f"{ident}  {name_node}: "
                       f"{value_to_string(value_1, level)}\n")

        elif node['status_tag'] == 'changed':
            result += (f"{ident}- {name_node}: "
                       f"{value_to_string(value_1, level)}\n")

            result += (f"{ident}+ {name_node}: "
                       f"{value_to_string(value_2, level)}\n")

        else:
            result += (f"{ident}  {name_node}: "
                       f"{stylish(node['nested'], level)}\n")

    result += f"{ident_bracket}" + "}"
    return result
