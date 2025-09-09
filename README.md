# CLIGenix

Intelligent Command-Line Interface Generation Using Large Language Models

## Overview

CLIGenix is a Python project for generating intelligent command-line interfaces, leveraging large language models. It is built with [Typer](https://typer.tiangolo.com/) for intuitive CLI development.

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/abandonedmonk/CLIGenix.git
cd CLIGenix
```

### 2. (Optional) Create and Activate a Conda Environment

If you use Conda for environment management:

```sh
conda create -n cligenix-env python=3.11
conda activate cligenix-env
```

### 3. Install Poetry

If Poetry is not already installed:

```sh
pip install poetry
```

or

```sh
conda install poetry
```

### 4. Install Project Dependencies

```sh
poetry install
```

This will install all required dependencies as specified in `pyproject.toml`.

### 5. (Optional) Activate the Poetry Shell

```sh
poetry shell
```

## Usage

After installation, you can run the CLI as follows:

```sh
poetry run cligenix
```

Or, if you installed it globally, simply:

```sh
cligenix
```

## Testing

To run the tests:

```sh
poetry run pytest
```

## Acknowledgments

- This project was inspired by and bootstrapped using the excellent [cookiecutter-typer](https://github.com/chamoda/cookiecutter-typer) template.
- Thanks to the [Typer](https://github.com/tiangolo/typer) library for making CLI development easy and enjoyable.
