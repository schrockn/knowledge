.PHONY: format check

format:
	.venv/bin/knowledge lint

check:
	.venv/bin/knowledge lint --check