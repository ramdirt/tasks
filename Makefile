.DEFAULT_GOLAD := help

run: ## start server
	poetry run uvicorn main:app --reload

install:
	poetry add $(LIBBARY)

uninstall:
	poetry remove $(LIBBARY)

help: ## help command
	@echo "Help"
