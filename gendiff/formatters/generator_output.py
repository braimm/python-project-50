from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def generate_output(diff, format='stylish'):
    match format:
        case 'stylish':
            oputput = stylish(diff)
        case 'plain':
            oputput = plain(diff)
            oputput = oputput[:len(oputput) - 1]
        case 'json':
            oputput = json(diff)
    return oputput
