# Modern Python Project Cookbook

This cookbook provides step-by-step instructions for creating a modern Python project with best practices for tooling, packaging, and structure. Includes optional CLI setup.

## Project Structure

Create the following directory structure:

```
project_name/
├── pyproject.toml
├── Makefile
├── src/
│   └── project_name/
│       ├── __init__.py
│       └── cli.py
└── README.md
```

## Step 1: Create Directory Structure

```bash
mkdir -p $PROJECT_NAME/src/$PROJECT_NAME
cd $PROJECT_NAME
```

## Step 2: Create pyproject.toml

Create `pyproject.toml` with modern Python packaging configuration:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "$PROJECT_NAME"
version = "0.1.0"
description = "Description of your project"
readme = "README.md"
authors = [
    {name = "$AUTHOR_NAME", email = "$AUTHOR_EMAIL"}
]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]
requires-python = ">=3.8"
dependencies = [
    # Add your project dependencies here
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "pytest-cov",
    "ruff>=0.1.0",
    "pyright",
]

# Optional: Add CLI entry point if building a command-line tool
# [project.scripts]
# $PROJECT_NAME = "$PROJECT_NAME.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.ruff]
target-version = "py313"
line-length = 100

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.pyright]
pythonVersion = "3.13"
typeCheckingMode = "basic"
reportMissingImports = true
reportMissingTypeStubs = false
```

## Step 3: Create Package Files

### src/$PROJECT_NAME/**init**.py

```python
"""Your project description."""

__version__ = "0.1.0"
```

### src/$PROJECT_NAME/main.py (or cli.py for CLI projects)

```python
"""Main module for your project."""

def main():
    """Main function."""
    print("Hello from $PROJECT_NAME!")


if __name__ == "__main__":
    main()
```

### Optional: CLI with Click (for command-line tools)

If building a CLI tool, also add dependencies and create a CLI module:

1. Add to pyproject.toml dependencies:

   ```toml
   dependencies = [
       "click>=8.0.0",
   ]

   [project.scripts]
   $PROJECT_NAME = "$PROJECT_NAME.cli:main"
   ```

2. Create `src/$PROJECT_NAME/cli.py`:

   ```python
   """CLI entry point for your project."""

   import click
   from pathlib import Path


   @click.group()
   @click.version_option()
   def main():
       """Your CLI description."""
       pass


   @main.command()
   @click.argument('name')
   def hello(name):
       """Say hello to NAME."""
       click.echo(f"Hello, {name}!")


   if __name__ == "__main__":
       main()
   ```

## Step 4: Create Makefile

Create a `Makefile` with common development commands:

```makefile
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

type-check:  ## Run type checking with pyright
	pyright src/

test:  ## Run tests
	pytest

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
```

## Step 5: Install and Test

1. Install in development mode:

   ```bash
   make dev-install
   ```

2. Test your project:

   ```bash
   python -m $PROJECT_NAME.main
   # Or if you created a CLI: $PROJECT_NAME hello World
   ```

3. Run linting and formatting:

   ```bash
   make check
   make fix
   ```

4. Run type checking:
   ```bash
   make type-check
   ```

## Key Features

- **Modern packaging**: Uses `pyproject.toml` with setuptools backend
- **Src layout**: Follows best practices with `src/` directory structure
- **Ruff integration**: Fast linting and formatting with comprehensive rules
- **Type checking**: Pyright support for static analysis
- **Optional CLI framework**: Click integration for command-line tools
- **Development workflow**: Makefile with common development tasks
- **Editable install**: Easy development with `pip install -e .`

## Template Variables

Before using this cookbook, define these variables:

```bash
export PROJECT_NAME="your_project_name"
export AUTHOR_NAME="Your Full Name"
export AUTHOR_EMAIL="your.email@example.com"
```

Then use find-and-replace or `envsubst` to substitute variables throughout the template files:

```bash
# Using envsubst to substitute variables in files
envsubst < template_file > actual_file
```

## Customization

1. Set the template variables above with your actual values
2. Add your project-specific dependencies to the `dependencies` list in `pyproject.toml`
3. Modify the main module or add CLI commands if building a command-line tool
4. Adjust ruff rules in `pyproject.toml` if needed

## Next Steps

- Add tests in a `tests/` directory
- Create a proper README.md with usage instructions
- Add CI/CD configuration (GitHub Actions, etc.)
- Consider adding pre-commit hooks
- Add more comprehensive CLI commands as needed
