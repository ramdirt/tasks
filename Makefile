.DEFAULT_GOLAD := help

run: ## start server
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .local.env

add:
	poetry add $(LIBRARY)

remove:
	poetry remove $(LIBRARY)

help: ## help command
	@echo "Help"

migrate-create:
	poetry run alembic revision --autogenerate -m $(MIGRATION)
