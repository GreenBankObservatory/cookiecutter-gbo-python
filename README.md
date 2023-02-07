# Cookiecutter GBO Python

Cookiecutter template for a "standard" GBO Python package

Based on: https://github.com/audreyfeldroy/cookiecutter-pypackage/

## Quickstart

Install cookiecutter, e.g via [pipx](https://github.com/pypa/pipx#on-linux-install-via-pip-requires-pip-190-or-later)

```bash
pipx install cookiecutter
```

Create your project interactively:

```bash
cookiecutter https://github.com/GreenBankObservatory/cookiecutter-gbo-python
```

Or, you can create it a bit quicker if you trust the defaults. For example, to create a project named `fooproj` with everything else set to default values:

```bash
cookiecutter https://github.com/GreenBankObservatory/cookiecutter-gbo-python project_name=fooproj --no-input
```

You will probably also want to create a simple config file at `~/.cookiecutterrc`. e.g.:

```
default_context:
    full_name: ""
    email: ""
    github_username: ""
    pypi_username: ""
```

## Background

The problem we're trying to solve: Python packaging is complicated and stupid. We want to be able to easily:

- Create a python package skeleton, based on a standardized template
    - LICENSE
    - README.md
    - pyproject.toml
- Install linters and code formatters
- Install pre-commit and relevant hooks
- Create a virtual environment for this package
- Install our dependencies, and our package itself, into the new venv

This is basically an implementation of what I consider best practices, and what I end up doing by hand for most of my new scripts/packages. But hopefully it's useful for others too
