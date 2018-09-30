FROM python:2.7-slim

run pip install pyserial requests

WORKDIR /app

COPY . /app

CMD ["python", "get_readings.py"]
