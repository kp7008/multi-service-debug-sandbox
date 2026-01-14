# Changelog

All notable changes to MSDS will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- Advanced request tracing visualization
- Custom failure injection scenarios
- Performance profiling tools
- Distributed debugging UI
- Integration with popular IDEs

## [0.1.0-alpha] - 2026-01-13

### Added
- Initial MSDS project generator
  - Python script to scaffold microservices projects
  - Automated file structure creation
  - Template-based configuration
  
- Security hardening module
  - Non-root container enforcement
  - API key authentication framework
  - Network isolation patterns
  - Read-only filesystem configuration
  - Capability dropping implementation
  
- Docker Compose orchestration
  - Multi-service setup and teardown
  - Network configuration
  - Environment variable management
  - Volume mounting for development
  
- Microservices skeleton
  - API Gateway service
  - Auth Service
  - User Service
  - Payment Service
  - MSDS Engine (control plane)
  
- Jaeger tracing integration
  - Distributed trace collection
  - Trace visualization
  - Service dependency mapping
  
- Developer tooling
  - Makefile with common commands
  - Health check utilities
  - Log aggregation
  - Service status monitoring
  
- CI/CD pipelines with security
  - GitHub Actions workflows
  - Trivy vulnerability scanning
  - Bandit security linting
  - Python code quality checks
  - Docker image building
  
- Comprehensive documentation
  - README with quick start
  - Security guidelines (SECURITY.md)
  - Contributing guidelines (CONTRIBUTING.md)
  - Original work documentation (ORIGINAL_WORK.md)
  - Attribution guidelines (ATTRIBUTION.md)
  - Authors and changelog
  - MIT License

### Features
- CLI tool for sandbox management (`msds` command)
- Environment-based configuration
- Production-ready security patterns
- Local development workflow
- Multi-service orchestration
- Integrated tracing and logging

### Testing
- Basic pytest setup
- Health check tests
- Service availability tests

### Documentation
- Quick start guide
- Architecture overview
- Security hardening guide
- Deployment instructions
- Contributing guidelines

### Creator
- **Pratik Koshiya** - Original design, architecture, and implementation (Jan 13, 2026)

---

## Versioning Strategy

- **Major (X.0.0)**: Breaking changes
- **Minor (0.X.0)**: New features (backwards compatible)
- **Patch (0.0.X)**: Bug fixes (backwards compatible)

Alpha/Beta labels used before v1.0.0 release.

## Release Process

1. Update CHANGELOG.md with changes
2. Update version in code
3. Commit: `git commit -m "Release version X.Y.Z"`
4. Tag: `git tag -a vX.Y.Z -m "Release X.Y.Z"`
5. Push: `git push && git push --tags`
6. Create GitHub Release

---

For detailed changelog history, see git log.
