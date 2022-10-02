# pyroject starter

This is a template for a python project. It uses [poetry](https://python-poetry.org/) for dependency management.

## Demo project

The project contains the following projects under `src`:

- Multi-layer PDF: This is a simple tool to merge multiple PDF files into a single PDF file.

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

# Check install poetry lock file
pip install poetry-lock-check==0.1.0
python3 -m poetry_lock_check check-lock
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
