**NOTICE: This project is no longer maintained. Please see the updated project: https://github.com/optivem/shop**

# ATDD Accelerator Template (Python)

[![commit-stage-monolith](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/commit-stage-monolith.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/commit-stage-monolith.yml)
[![acceptance-stage](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/acceptance-stage.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/acceptance-stage.yml)
[![qa-stage](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-stage.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-stage.yml)
[![qa-signoff](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-signoff.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-signoff.yml)
[![prod-stage](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/prod-stage.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/prod-stage.yml)

This is a Python implementation of the ATDD (Acceptance Test-Driven Development) Accelerator Template. It provides a walking skeleton for building applications using Test-Driven Development practices with Python and FastAPI.

## Structure

- **`monolith/`** - Main FastAPI application with walking skeleton implementation
- **`system-test/`** - End-to-end and system tests for acceptance testing
- **`.github/`** - CI/CD workflows for commit, acceptance, QA, and production stages

## Quick Start

```bash
# Run the application
cd monolith
python -m uvicorn src.main:app --reload --port 8080

# Run tests  
cd system-test
pytest . -m smoke
```

See individual component READMEs for detailed setup instructions:
- [`monolith/README.md`](monolith/README.md) - Application setup and development
- [`system-test/README.md`](system-test/README.md) - Testing setup and execution

## License

[![Unlicense](https://img.shields.io/badge/license-Unlicense-lightgrey.svg)](http://unlicense.org/)

This project is released under [The Unlicense](http://unlicense.org) — a public domain dedication.

## Contributors

- [Valentina Jemuović](https://github.com/valentinajemuovic)
- [Jelena Cupać](https://github.com/jcupac)
