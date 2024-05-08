install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet-code --cov-report xml

check:
	poetry run flake8 gendiff
	poetry run flake8 tests
	poetry run pytest
