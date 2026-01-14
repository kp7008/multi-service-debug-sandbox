# MSDS - Multi-Service Debug Sandbox
.PHONY: help up down build logs status health test clean docker-clean reset

help:
	@echo "🔧 MSDS Production"
	@echo "  make build       - Build images"
	@echo "  make up          - Start services"
	@echo "  make health      - Check status"

up:
	docker compose up -d --build

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

status:
	docker compose ps

health:
	@curl -s localhost:5000/health && echo "✅ API OK" || echo "⏳ API"
	@curl -s localhost:8000/health && echo "✅ Engine OK" || echo "⏳ Engine"

test:
	pytest -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

docker-clean:
	docker compose down -v

reset: clean docker-clean

.DEFAULT_GOAL := help