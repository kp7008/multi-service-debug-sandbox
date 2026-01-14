# MSDS - Multi-Service Debug Sandbox

IDE-like debugging sandbox for microservices

## Quick Start

```bash
make build
make up
make health
```

## Access Points

- API Gateway: http://localhost:5000
- MSDS Engine: http://localhost:8000
- Jaeger UI: http://localhost:16686

## Commands

```bash
make up          # Start all services
make down        # Stop services
make logs        # View logs
make health      # Check health
make test        # Run tests
make clean       # Cleanup
```