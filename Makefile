install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest

check:
	poetry run flake8 gendiff
	poetry run flake8 tests
	poetry run pytest

test-cov:
	poetry run coverage run -m pytest
	poetry run coverage report

diff_yml:
	poetry run gendiff tests/fixtures/file1.1.json tests/fixtures/file2.1.json

diff_plain:
	poetry run gendiff tests/fixtures/file1.1.yml tests/fixtures/file2.1.yml -f plain

diff_json:
	poetry run gendiff tests/fixtures/file1.1.yml tests/fixtures/file2.1.yml -f json

diff:
	poetry run gendiff -h