# Security Guidelines for MSDS

## Local Development
- API keys stored in `.env` (never committed)
- Services only accessible on localhost
- Non-root containers
- Read-only filesystems

## Staging/Production
- All secrets in environment variables
- TLS/HTTPS enabled
- Rate limiting active
- Network policies enforced
- Security scanning in CI/CD

## Reporting Vulnerabilities
Email: security@yourcompany.com

## Security Checklist
- [ ] .env in .gitignore
- [ ] Non-root user in containers
- [ ] API authentication enabled
- [ ] Read-only filesystems
- [ ] Secrets in GitHub Actions
- [ ] Network isolation (localhost only)
- [ ] CI/CD security scanning

## Key Files
- `.env` - Local secrets (NOT committed)
- `.env.example` - Template (safe to commit)
- `secrets/` - Directory for local secrets
- `SECURITY.md` - This file
