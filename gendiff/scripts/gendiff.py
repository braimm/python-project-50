#!/usr/bin/env python3
from gendiff import argparser
from gendiff import generate_diff


def main():
    paths = argparser.get_args()
    diff = generate_diff.generate_diff(paths.first_file, paths.second_file)
    print(diff)


if __name__ == "__main__":
    main()