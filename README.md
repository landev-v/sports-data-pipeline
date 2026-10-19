# sports-data-pipeline

A Python pipeline that pulls official data from the MLB Stats API and produces a descriptive report comparing a starting pitcher's performance across two seasons, normalized against the league average for starting pitchers.

> **Project status:** early development (v0.1.0). The v1.0 scope is defined in [`docs/scope.md`](docs/scope.md) (in Spanish). Metric calculations are in progress.

## What v1.0 will do

Given a pitcher's MLB ID and two seasons, the program will report on the pitcher's starts only (relief appearances are excluded):

- **Core metrics:** K%, BB%, K-BB% and HR/9, expressed as an index where 100 equals the league average for starting pitchers in each season, with a descriptor based on FanGraphs thresholds.
- **Sample context:** starts, innings pitched and outs per start.
- **Complementary metrics:** ERA, FIP, WHIP and BABIP as raw values.
- **An interactive chart** comparing both seasons, also saved as a PNG image.

The report describes what changed between seasons. It does not make predictions or judgments.

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

_Not available yet. The command-line interface is planned for v1.0; see the [scope document](docs/scope.md) for details._

## Running tests

With the development dependencies installed, run:

```bash
pytest
```

To check test coverage:

```bash
pytest --cov=sports_pipeline --cov-report=term-missing
```

Tests do not require an internet connection.

## Development conventions

- Type hints and Google-style docstrings throughout the code.
- Tests written alongside each feature.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About this project

This project is part of a structured learning effort in data pipelines, software architecture and descriptive statistics, built around sports data I follow closely. Feedback and discussion are welcome.
