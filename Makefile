# Define targets
.PHONY: pretty test

pretty: isort black

black:
	black . --exclude env/

isort:
	isort . --skip env/

test_ml:
	pytest tests/test_ml.py

test_app:
	pytest tests/test_app.py
	