.PHONY: help install dev-install lint format check test clean

help:  ## Show this help message
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package
	pip install .

dev-install:  ## Install the package in development mode
	pip install -e .[dev]

lint:  ## Run ruff linter
	ruff check src/

format:  ## Format code with ruff
	ruff format src/

check:  ## Run both linting and formatting checks
	ruff check src/
	ruff format --check src/

fix:  ## Auto-fix linting issues and format code
	ruff check --fix src/
	ruff format src/

type-check:  ## Run type checking with mypy
	mypy src/

pyright:  ## Run type checking with pyright
	pyright src/

test:  ## Run tests
	pytest

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete