# pyroject starter

[![license][license-image]][repository-url]
[![Build Status][build-status-image]][build-status]
[![Sourcegraph][sg-image]][sg-url]
[![Release Date][rle-image]][rle-url]
[![GitHub repo size][repo-size-image]][repository-url]

[repo-size-image]: https://img.shields.io/github/repo-size/funnyzak/pyproject-starter
[build-status-image]: https://img.shields.io/github/workflow/status/funnyzak/pyproject-starter/CI
[build-status]: https://github.com/funnyzak/pyproject-starter/actions
[license-image]: https://img.shields.io/github/license/funnyzak/pyproject-starter.svg?style=flat-square
[repository-url]: https://github.com/funnyzak/pyproject-starter
[sg-image]: https://img.shields.io/badge/view%20on-Sourcegraph-brightgreen.svg?style=flat-square
[sg-url]: https://sourcegraph.com/github.com/funnyzak/pyproject-starter
[rle-image]: https://img.shields.io/github/release-date/funnyzak/pyproject-starter.svg
[rle-url]: https://github.com/funnyzak/pyproject-starter/releases/latest

a template for a python project. It uses [poetry](https://python-poetry.org/) for dependency management and [tox](https://github.com/tox-dev/tox) for testing.

## Demo project

The project contains the following projects under `src`:

- [Hello](https://github.com/funnyzak/pyproject-starter/tree/main/src/hello): a simple hello world project
- [PDF_Parse](https://github.com/funnyzak/pyproject-starter/tree/main/src/pdf_parse): a project that parse pdf.

## Prerequisite

- [^Python 3.7](https://www.python.org/)
- [^Poetry 1.2](https://python-poetry.org/)

## Usages

```bash
# Install dependencies
# Install dependencies with all extras
poetry install --all-extras
# Install dependencies with extras 'pdf'
poetry install --extras "pdf"
# Only install required dependencies
poetry install

# Run project => hello
poetry run hello

# Lint with black
poetry run black ./src --check

# Format with black
poetry run black ./src

# Check with mypy
poetry run mypy ./src

# Check import order with isort
poetry run isort ./src --check

# Lint with flake8
poetry run flake8 ./src
```

## References

- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/user/adding-pdf-annotations.html#free-text): a library for working with PDF files.
- [flake8](https://flake8.pycqa.org/en/latest/): a wrapper around these tools: PyFlakes, pycodestyle, and Ned Batchelder’s McCabe script.
- [isort](https://pycqa.github.io/isort/): a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
- [black](https://black.readthedocs.io/en/stable/): a Python code formatter.
- [mypy](https://mypy.readthedocs.io/en/stable/config_file.html#per-module-and-global-options): a static type checker for Python.

## FAQ

### Install

#### install poetry

See [poetry installation](https://python-poetry.org/docs/#installation).

#### install python3

See [python installation](https://www.python.org/downloads/).

## Contribution

If you have any questions or suggestions, please feel free to open an issue or pull request.

<a href="https://github.com/funnyzak/pyproject-starter/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=funnyzak/pyproject-starter" />
</a>

## License

MIT License © 2022 [funnyzak](https://github.com/funnyzak)
