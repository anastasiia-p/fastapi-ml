FROM python:3.11

COPY requirements.txt requirements-dev.txt setup.py /workdir/
COPY app/ /workdir/app/
COPY ml/ /workdir/ml/

WORKDIR /workdir

RUN pip install -U -e .

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]