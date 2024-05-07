#!/usr/bin/env python3
from gendiff import cli_args
from gendiff import generate_diff


def main():
    args = cli_args.get_args()
    diff = generate_diff.generate_diff(
        args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
