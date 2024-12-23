format:
	@echo "formatting..."
	poetry run ruff format app

types:
	@echo "checking types..."
	poetry run mypy app

run:
	@echo "running app'ку..."
	poetry run python cli.py api
