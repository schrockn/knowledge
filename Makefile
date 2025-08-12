.PHONY: format check

format:
	.venv/bin/knowledge check md --fix

check:
	.venv/bin/knowledge check md