FROM python:3.11-slim

WORKDIR /app

RUN useradd -m -u 1000 appuser

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY msds-engine/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY msds-engine/ .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000
CMD ["python", "app.py"]
