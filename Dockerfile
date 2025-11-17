FROM python:3.11-slim

WORKDIR /app
COPY app/requirements-test.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements-test.txt
COPY app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]