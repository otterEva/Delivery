format:
	@echo "formatting..."
	poetry run ruff format app

types:
	@echo "checking types..."
	poetry run mypy app

run:
	@echo "checking types..."
	poetry run app.main:app --reload
