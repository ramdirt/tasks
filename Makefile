.DEFAULT_GOLAD := help

run: ## start server
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .local.env

install:
	poetry add $(LIBBARY)

uninstall:
	poetry remove $(LIBBARY)

help: ## help command
	@echo "Help"
