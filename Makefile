.PHONY: format check

format:
	.venv/bin/knowledge check md --fix
	$(MAKE) -C python/knowledge format

check:
	.venv/bin/knowledge check md
	$(MAKE) -C python/knowledge check