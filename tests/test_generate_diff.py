# import pytest
# import os
from gendiff.generate_diff import generate_diff


def test_generate_diff():
    diff_file = open('tests/fixtures/diff.txt')
    reference = diff_file.read()
    diff_file.close()
    path_file_1 = 'tests/fixtures/file1.json'
    path_file_2 = 'tests/fixtures/file2.json'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference

    path_file_1 = 'tests/fixtures/file1.yml'
    path_file_2 = 'tests/fixtures/file2.yml'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference

    path_file_1 = 'tests/fixtures/file1.yaml'
    path_file_2 = 'tests/fixtures/file2.yaml'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference

    diff_nested_file = open('tests/fixtures/diff_nested.txt')
    reference = diff_nested_file.read()
    diff_nested_file.close()
    path_file_1 = 'tests/fixtures/file_nested_1.json'
    path_file_2 = 'tests/fixtures/file_nested_2.json'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference

    diff_nested_to_plain_file = open('tests/fixtures/diff_nested_to_plain.txt')
    reference = diff_nested_to_plain_file.read()
    diff_nested_to_plain_file.close()
    path_file_1 = 'tests/fixtures/file_nested_1.json'
    path_file_2 = 'tests/fixtures/file_nested_2.json'
    result = generate_diff(path_file_1, path_file_2, 'plain')
    assert result == reference
