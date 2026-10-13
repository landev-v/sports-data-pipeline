# sports-data-pipeline

A modular Python pipeline for ingesting and analyzing mlb data from multiple sources.

> **Project status:** Early development (v0.1.0). Foundation and first fetcher in progress.

## Features

- **Modular fetcher architecture**: abstract base class with concrete implementations for each data source.
- **Type-safe and tested**: full type hints and unit tests from the first commit.
- **Strict configuration**: centralized in `pyproject.toml` following modern Python packaging standards.

## Requirements

- Python 3.11 or higher
- Git
- Operating system: Windows, macOS, or Linux

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/landev-v/sports-data-pipeline.git
cd sports-data-pipeline
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows (PowerShell)
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

Install the project in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

_This section will be populated as features are implemented. The first fetcher (MLB Stats API) is currently under development._

## Project structure

```
sports-data-pipeline/
├── src/
│   └── sports_pipeline/
│       ├── __init__.py
│       └── fetchers/
│           ├── __init__.py
│           ├── base.py        # Abstract BaseFetcher
│           └── mlb.py         # MLB Stats API fetcher
├── tests/
│   ├── __init__.py
│   └── fetchers/
│       ├── __init__.py
│       ├── test_base.py
│       └── test_mlb.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Running tests

With the development dependencies installed, run:

```bash
pytest
```

To check test coverage:

```bash
pytest --cov=sports_pipeline --cov-report=term-missing
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About this project

This project is part of a structured learning effort focused on data pipelines, statistical modeling, and software architecture. It serves both as a technical exercise in building production-grade Python systems and as a foundation for sports analytics work. Contributions, feedback, and discussions are welcome.
