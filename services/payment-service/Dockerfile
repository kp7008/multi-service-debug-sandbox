FROM python:3.11-slim

WORKDIR /app

RUN useradd -m -u 1000 appuser

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY services/payment-service/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY services/payment-service/ .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5003
CMD ["python", "main.py"]
