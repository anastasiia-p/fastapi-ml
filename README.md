## Local development

```bash
# Create a virtual environment
python3.11 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install/upgrade development dependencies
pip install -U -e .
pip install -U -e .[dev]

# (Optional) Code formatting
make pretty

# Run app
uvicorn app.app:app --host 0.0.0.0 --port 8080

# Run tests
make test

# Deactivate the virtual environment
deactivate
```

## Run app in docker container

```bash
docker build -t ml-app .
docker run -p 80:80 ml-app
```

## Run tests while docker container is running (in other terminal)

```bash
source env/bin/activate
make test

deactivate
```