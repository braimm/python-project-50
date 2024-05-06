#!/usr/bin/env python3
from gendiff import cli_args
from gendiff import generate_diff
from gendiff.generator_output import generate_output


def main():
    args = cli_args.get_args()
    diff = generate_diff.generate_diff(args.first_file, args.second_file)
    print(args.format)
    formatted_output = generate_output(diff, args.format)
    print(formatted_output)


if __name__ == "__main__":
    main()
