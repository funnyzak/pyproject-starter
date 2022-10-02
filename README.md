# pyroject starter

[![license][license-image]][repository-url]
[![Build Status][build-status-image]][build-status]
[![Sourcegraph][sg-image]][sg-url]
[![Release Date][rle-image]][rle-url]
[![GitHub repo size][repo-size-image]][repository-url]

[repo-size-image]: https://img.shields.io/github/repo-size/funnyzak/pyproject-starter
[build-status-image]: https://img.shields.io/github/workflow/status/funnyzak/pyproject-starter/lint-and-test
[build-status]: https://github.com/funnyzak/pyproject-starter/actions
[license-image]: https://img.shields.io/github/license/funnyzak/pyproject-starter.svg?style=flat-square
[repository-url]: https://github.com/funnyzak/pyproject-starter
[sg-image]: https://img.shields.io/badge/view%20on-Sourcegraph-brightgreen.svg?style=flat-square
[sg-url]: https://sourcegraph.com/github.com/funnyzak/pyproject-starter
[rle-image]: https://img.shields.io/github/release-date/funnyzak/pyproject-starter.svg
[rle-url]: https://github.com/funnyzak/pyproject-starter/releases/latest

This is a template for a python project. It uses [poetry](https://python-poetry.org/) for dependency management.

## Demo project

The project contains the following projects under `src`:

- [Hello](https://github.com/funnyzak/pyproject-starter/tree/main/src/hello): a simple hello world project
- [Multi-layer PDF](https://github.com/funnyzak/pyproject-starter/tree/main/src/multi_layer_pdf): This is a simple tool to merge multiple PDF files into a single PDF file.

## Prerequisite

- [Python 3](https://www.python.org/)
- [poetry](https://python-poetry.org/)

## Commands

```bash
# Install dependencies
poetry install

# Lint with black
poetry run black ./src --check

# Format with black
poetry run black ./src

# Check with mypy
poetry run mypy ./src

# Check import order with isort
poetry run isort ./src --check

# Lint with flake8
poetry run flake8 ./src --count --show-source --statistics --ignore=E501
```

## Project Usage

```bash
# Run Hello Project 
poetry run hello
```

## Resources

- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/user/adding-pdf-annotations.html#free-text)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [isort](https://pycqa.github.io/isort/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](https://mypy.readthedocs.io/en/stable/config_file.html#per-module-and-global-options)

## Author

| [![twitter/funnyzak](https://s.gravatar.com/avatar/c2437e240644b1317a4a356c6d6253ee?s=70)](https://twitter.com/funnyzak 'Follow @funnyzak on Twitter') |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [funnyzak](https://yycc.me/)                                                                                                                           |

## License

MIT License © 2022 [funnyzak](https://github.com/funnyzak)
