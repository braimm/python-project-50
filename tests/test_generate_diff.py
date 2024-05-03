# import pytest
# import os
from gendiff.generate_diff import generate_diff



def test_generate_diff():
    diff_file = open('tests/fixtures/diff.txt')
    reference = diff_file.read()
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
    assert result == reference
    