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
## **When to Use MSDS - Real-World Scenarios**

Your MSDS (Multi-Service Debug Sandbox) solves **microservices pain points**. Here's when and how:

***

## **🎯 Real Scenario 1: Debugging Cross-Service Failures**

**Problem:** Your payment service calls user service, which calls auth service. Request fails somewhere in the chain, but you don't know where.

**Without MSDS:**
- SSH into 3 different servers
- `tail -f logs` on each
- Manually trace request flow
- **Takes 30+ minutes**

**With MSDS:**
```bash
cd my-msds-project
make up
# Visit http://localhost:16686 (Jaeger)
# See ENTIRE request path in one place
# Identify exact failure point in seconds
```

✅ **Result:** Find bottleneck in 2 minutes vs 30+ minutes

***

## **🎯 Real Scenario 2: Test Version Skew Issues**

**Problem:** You upgraded API Gateway to v2 but other services still v1. Does it work?

**Without MSDS:**
- Deploy to staging
- Run full test suite
- Fix integration issues in prod
- **Causes outages**

**With MSDS:**
```bash
# Edit docker-compose.yml - change API Gateway version
api-gateway:
  image: myrepo/api-gateway:v2  # Changed!

make rebuild
make up
make health
# Test locally BEFORE deploying
```

✅ **Result:** Catch version conflicts before prod

***

## **🎯 Real Scenario 3: Chaos Engineering - Inject Failures**

**Problem:** How will your system behave when payment service is slow?

**Without MSDS:**
- Take production down
- Run chaos tests
- Hope nothing breaks

**With MSDS:**
```bash
# Inject 2-second latency into payment service
docker exec my-msds-project-payment-service-1 \
  tc qdisc add dev eth0 root netem delay 2000ms

# Test your retry logic
curl http://localhost:5000/api/charge

# Watch in Jaeger how services respond
```

✅ **Result:** Test failure scenarios safely locally

***

## **🎯 Real Scenario 4: Onboarding New Developers**

**Problem:** New dev joins team. Setup takes 2 days (install 15 services, configure databases, set environment variables).

**Without MSDS:**
- Run 20 manual setup steps
- Debug environment issues
- **Very slow onboarding**

**With MSDS:**
```bash
# New dev just does:
git clone https://github.com/yourteam/msds.git
cd multi-service-debug-sandbox
make build
make up

# Full microservices stack running in 5 minutes!
```

✅ **Result:** New dev productive on day 1

***

## **🎯 Real Scenario 5: Load Testing Individual Services**

**Problem:** Which service is the bottleneck?

**Without MSDS:**
- Load test production
- Risk taking down real users
- Expensive infrastructure

**With MSDS:**
```bash
# Run load test locally against user-service
ab -n 1000 -c 50 http://localhost:5002/users

# Watch Jaeger to see service behavior under load
# See response times, error rates in real-time
```

✅ **Result:** Identify bottlenecks safely, locally, free

***

## **🎯 Real Scenario 6: Reproducing Bug Report**

**Problem:** User reports "payments fail when user from France." How do you reproduce?

**Without MSDS:**
- Manually setup test environment
- Try to recreate conditions
- Hard to debug

**With MSDS:**
```bash
# Add test code to auth-service
# Simulate France-based user
# Inject failure
# Run locally with full tracing

make up
# Test payment flow with France user
# See exactly where it fails in Jaeger
```

✅ **Result:** Reproduce + fix bugs faster

***

## **How to Use for Each Scenario**

### **Scenario 1: Tracing Requests**
```bash
make up
# Open http://localhost:16686
# Make request: curl http://localhost:5000/api/ping
# See full trace in Jaeger
```

### **Scenario 2: Version Testing**
```bash
# Edit docker-compose.yml with new versions
make rebuild
make up
make test
```

### **Scenario 3: Failure Injection**
```bash
# Modify service code
# Add latency/errors
make up
# Test behavior
```

### **Scenario 4: Onboarding**
```bash
make build
make up
# New dev now has working stack
```

### **Scenario 5: Performance Testing**
```bash
make up
# Run load tests: ab, wrk, hey, k6
# Monitor in Jaeger
```

### **Scenario 6: Bug Reproduction**
```bash
# Modify test data in services
make up
# Reproduce bug locally
# Fix and verify
```

***

## **Key Commands for Troubleshooting**

```bash
# 1. Check which services are running
make status

# 2. View logs for specific service
docker compose logs -f payment-service

# 3. Check service health
make health

# 4. Access service directly
curl http://localhost:5000/health

# 5. Stop and clean everything
make reset

# 6. Rebuild specific service
docker compose build payment-service

# 7. Run tests
make test

# 8. View all logs
make logs
```

***

## **Why MSDS Solves Real Problems**

| Problem | Time Without MSDS | Time With MSDS | Savings |
|---------|-------------------|----------------|---------|
| Debug cross-service failure | 30+ min | 2-5 min | **85% faster** |
| Test version conflicts | 1-2 hours | 10 min | **90% faster** |
| Onboard new dev | 2 days | 1 hour | **95% faster** |
| Reproduce bug | 1+ hour | 10 min | **85% faster** |
| Load test | 2+ hours | 30 min | **75% faster** |

***

## **Your Next Steps**

1. **Run it locally** - Get comfortable with `make` commands
2. **Modify a service** - Change API endpoint, rebuild, test
3. **Add tracing** - Make requests, view in Jaeger
4. **Inject failures** - Simulate latency, test retry logic
5. **Share with team** - Push to GitHub, team can use same setup

**MSDS transforms microservices debugging from painful → simple.** 🚀
