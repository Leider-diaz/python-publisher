FROM python:3.10-slim

WORKDIR /app

RUN pip install fastapi uvicorn[standard] pika

COPY producer.py /app/

EXPOSE 8000

CMD ["uvicorn", "producer:app", "--host", "0.0.0.0", "--port", "8000"]