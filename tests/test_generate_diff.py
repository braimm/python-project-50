import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture
def reference_stylish():
    fixture_file = open('tests/fixtures/result_stylish.txt')
    fixture = fixture_file.read()
    fixture_file.close()
    return fixture


def test_generate_diff_json(reference_stylish):
    path_file_1 = 'tests/fixtures/file1.json'
    path_file_2 = 'tests/fixtures/file2.json'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference_stylish


def test_generate_diff_yaml(reference_stylish):
    path_file_1 = 'tests/fixtures/file1.yml'
    path_file_2 = 'tests/fixtures/file2.yml'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference_stylish

    path_file_1 = 'tests/fixtures/file1.yaml'
    path_file_2 = 'tests/fixtures/file2.yaml'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference_stylish


def test_generate_diff_nested_to_stylish():
    diff_nested_file = open('tests/fixtures/result_nested_stylish.txt')
    reference = diff_nested_file.read()
    diff_nested_file.close()
    path_file_1 = 'tests/fixtures/file_nested_1.json'
    path_file_2 = 'tests/fixtures/file_nested_2.json'
    result = generate_diff(path_file_1, path_file_2)
    assert result == reference


def test_generate_diff_nested_to_plain():
    diff_nested_to_plain_file = open('tests/fixtures/result_plain.txt')
    reference = diff_nested_to_plain_file.read()
    diff_nested_to_plain_file.close()
    path_file_1 = 'tests/fixtures/file_nested_1.json'
    path_file_2 = 'tests/fixtures/file_nested_2.json'
    result = generate_diff(path_file_1, path_file_2, 'plain')
    assert result == reference
