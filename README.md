### Tests and linter status:
[![Actions Status](https://github.com/braimm/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/braimm/python-project-50/actions)
[![Github Actions Status](https://github.com/braimm/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/braimm/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9aadb67621f709d2eac9/maintainability)](https://codeclimate.com/github/braimm/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9aadb67621f709d2eac9/test_coverage)](https://codeclimate.com/github/braimm/python-project-50/test_coverage)


## Description of project

**gendiff** - console utility that compares two configuration files and shows a difference.
Available formats files - **JSON** and **YAML**.

### SYNOPSIS: 
```bash
gendiff [-h] [-f FORMAT] <first_file> <second_file>
```
1. **-h**, **--help**   show this help message and exit
2. **-f FORMAT** or **--format FORMAT**   set format of output

## Install
### Required for installation:
1. pip (version 23.3.1 or newer)
2. Poetry (version 1.7.1 or newer)
### Installation steps:
1. Install Poetry
```bash
pip install poetry
```
2. Copy project from repository, manually or with the command
```bash
git clone git@github.com:braimm/python-project-50.git
```
3. Run inside the project's directory the following command to use the package as a **CLI** utility
```bash
make install_gendiff
```
4. Check that the program is available by name **gendiff**
```bash
gendiff -h
```

## Available output formats and examples of work:
1. **Stylish** (default option)
```bash
gendiff filepath1.json filepath2.json
```
        {
        - follow: false
            host: hexlet.io
        - proxy: 123.234.53.22
        - timeout: 50
        + timeout: 20
        + verbose: true
        }
2. **Plain**
```bash
gendiff filepath1.json filepath2.json --format plain 
```
        Property 'follow' was removed
        Property 'proxy' was removed
        Property 'timeout' was updated. From '50' to '20'
        Property 'verbose' was added with value: true
3. **JSON**
```bash
gendiff filepath1.yaml filepath2.yaml --format json
```
        [
            {
                "key": "follow",
                "value_1": false,
                "status_tag": "only_data_1"
            },
            {
                "key": "host",
                "value_1": "hexlet.io",
                "status_tag": "non_changed"
            },
            {
                "key": "proxy",
                "value_1": "123.234.53.22",
                "status_tag": "only_data_1"
            },
            {
                "key": "timeout",
                "value_1": 50,
                "value_2": 20,
                "status_tag": "changed"
            },
            {
                "key": "verbose",
                "value_1": true,
                "status_tag": "only_data_2"
            }
        ]



## Asciinema examples of work

1. **Generate diff STYLISH-format for plain JSON-files:**
https://asciinema.org/a/wNkLM7Nf7ipJ2bWwPVRGaY2Pu
[![asciicast](https://asciinema.org/a/wNkLM7Nf7ipJ2bWwPVRGaY2Pu.svg)](https://asciinema.org/a/wNkLM7Nf7ipJ2bWwPVRGaY2Pu)

2. **Generate diff STYLISH-format for plain YAML-files:**
https://asciinema.org/a/lug7bjTjFLGpfgogjhhh3m6Kt
[![asciicast](https://asciinema.org/a/lug7bjTjFLGpfgogjhhh3m6Kt.svg)](https://asciinema.org/a/lug7bjTjFLGpfgogjhhh3m6Kt)

3. **Generate diff in STYLISH-format for nested YAML/JSON-files:**
https://asciinema.org/a/q654jurmoURgoTPoR5EXs6zg8
[![asciicast](https://asciinema.org/a/q654jurmoURgoTPoR5EXs6zg8.svg)](https://asciinema.org/a/q654jurmoURgoTPoR5EXs6zg8)

4. **Generate diff in PLAIN-format for nested YAML/JSON-files:**
https://asciinema.org/a/HC9ZsQ1g5uO3aoaZatW23rT9Y
[![asciicast](https://asciinema.org/a/HC9ZsQ1g5uO3aoaZatW23rT9Y.svg)](https://asciinema.org/a/HC9ZsQ1g5uO3aoaZatW23rT9Y)

5. **Generate diff in JSON-format for nested YAML/JSON-files:**
https://asciinema.org/a/YLRxfBHefsnTkaFgk0ddqEfrR
[![asciicast](https://asciinema.org/a/YLRxfBHefsnTkaFgk0ddqEfrR.svg)](https://asciinema.org/a/YLRxfBHefsnTkaFgk0ddqEfrR)