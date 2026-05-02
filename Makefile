.PHONY: setup dev test

setup:
	@bash scripts/setup.sh

dev:
	@python3 -m axiom

test:
	@python3 -m pytest tests/ -q
