# PyPoject Starter

[![Build Status][build-status-image]][build-status]
[![license][license-image]][repository-url]
[![Sourcegraph][sg-image]][sg-url]
[![Release Date][rle-image]][rle-url]
[![GitHub repo size][repo-size-image]][repository-url]

A template for the python project. It uses [poetry](https://python-poetry.org/) for dependency management and [tox](https://github.com/tox-dev/tox) for testing.

[repo-size-image]: https://img.shields.io/github/repo-size/funnyzak/pyproject-starter
[build-status-image]:  https://github.com/funnyzak/pyproject-starter/actions/workflows/ci.yml/badge.svg
[build-status]: https://github.com/funnyzak/pyproject-starter/actions
[license-image]: https://img.shields.io/github/license/funnyzak/pyproject-starter.svg?style=flat-square
[repository-url]: https://github.com/funnyzak/pyproject-starter
[sg-image]: https://img.shields.io/badge/view%20on-Sourcegraph-brightgreen.svg?style=flat-square
[sg-url]: https://sourcegraph.com/github.com/funnyzak/pyproject-starter
[rle-image]: https://img.shields.io/github/release-date/funnyzak/pyproject-starter.svg
[rle-url]: https://github.com/funnyzak/pyproject-starter/releases/latest

## Features

- Use [poetry](https://python-poetry.org/) for dependency management.
- Use tox、pytest、pytest-cov、coverage for testing.
- Use black、isort for code formatting.
- Use flake8 for linting.
- Use mypy for static type checking.
- Use [pre-commit](https://pre-commit.com/) for code quality.
- Use ipdb3 for debugging.
- Multiple python versions support(Python 3.7+).
- More features to be added.

## Project

Contains the following projects under `src` as demo:

- [Hello](https://github.com/funnyzak/pyproject-starter/tree/main/src/hello) is a simple hello world project.
- [PDF_Parse](https://github.com/funnyzak/pyproject-starter/tree/main/src/pdf_parse) is a project that parse pdf.

## Prerequisite

- [^Python 3.7](https://www.python.org/)
- [^Poetry 1.2](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)

## Installation

following the steps below to setup the project:

```bash

```bash
# Clone the repository
git clone git@github.com:funnyzak/pyproject-starter.git && cd pyproject-starter

# Install all dependencies
poetry install --sync --all-extras --with dev,test,coverage

# Other useful installation dependencies commands
# Install dependencies with all extras
poetry install --all-extras
# Install dependencies with extras 'pdf' for pdf_parse project
poetry install --extras "pdf"
# Install dependencies with group 'dev'、'test' for development
poetry install --with dev,test
# Only install required dependencies for production
poetry install
```

## Usage

There are some useful commands for development:

```bash
# Run project => hello
poetry run hello

# Run project => pdf_parse: merge pdf
poetry run mergepdf

# Debug "hello" project with ipdb3
poetry run ipdb3 ./src/hello/main.py

# Code test
poetry run pytest
# or coverage test
poetry run tox

# Lint with black
poetry run black ./src --check

# Format code with black
poetry run black ./src

# Check with mypy
poetry run mypy ./src

# Check import order with isort
poetry run isort ./src --check

# Lint with flake8
poetry run flake8 ./src
```

## References

some useful references:

- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/user/adding-pdf-annotations.html#free-text) is a library for working with PDF files.
- [flake8](https://flake8.pycqa.org/en/latest/) is a wrapper around these tools: PyFlakes, pycodestyle, and Ned Batchelder’s McCabe script.
- [isort](https://pycqa.github.io/isort/) is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
- [black](https://black.readthedocs.io/en/stable/) is a Python code formatter.
- [mypy](https://mypy.readthedocs.io/en/stable/config_file.html#per-module-and-global-options) is a static type checker for Python.
- [pytest](https://docs.pytest.org/en/stable/) is a testing framework for Python.
- [ipdb](https://pypi.org/project/ipdb/) is a IPython-enabled pdb.

## FAQ

### Development

### How to add a new project?

1. Create a new folder under `src` folder.
2. You can copy the `hello` project as a template.
3. Add folder name to `packages` in `pyproject.toml` file.
4. Code and test it.
5. You can create test cases for the new project in `tests` folder.

### Environment setup

#### install poetry

See [poetry installation](https://python-poetry.org/docs/#installation).

#### install python3

See [python installation](https://www.python.org/downloads/).

#### install pre-commit

See [pre-commit installation](https://pre-commit.com/#install).

## Contribution

If you have any questions or suggestions, please feel free to open an issue or pull request.

<a href="https://github.com/funnyzak/pyproject-starter/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=funnyzak/pyproject-starter" />
</a>

## License

MIT License © 2022 [funnyzak](https://github.com/funnyzak)
