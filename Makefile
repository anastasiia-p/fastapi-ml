# Define targets
.PHONY: pretty test

pretty: isort black

black:
	black . --exclude env/

isort:
	isort . --skip env/

test:
	pytest tests/
	