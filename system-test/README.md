# System Tests

End-to-end and system tests for the ATDD Accelerator Template application.

## Overview

This directory contains system tests that verify the application works correctly when deployed. The tests are designed to run against a live instance of the application.

## Test Types

- **Smoke Tests** (`@pytest.mark.smoke`) - Basic functionality verification
- **E2E Tests** (`@pytest.mark.e2e`) - End-to-end user scenarios

## Test Files

- `test_api_smoke.py` - API smoke tests
- `test_api_e2e.py` - API end-to-end tests  
- `test_ui_smoke.py` - UI smoke tests
- `test_ui_e2e.py` - UI end-to-end tests

## Prerequisites

- Python 3.11 or higher
- Running application instance (http://localhost:8080)

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the application with Docker:**
   ```bash
   docker compose up -d
   ```

## Running Tests

### All Tests
```bash
pytest .
```

### Smoke Tests Only
```bash
pytest . -m smoke
```

### E2E Tests Only
```bash
pytest . -m e2e
```

### Verbose Output
```bash
pytest . -v
```

### Specific Test File
```bash
pytest test_api_smoke.py
```

## Cleanup

```bash
docker compose down
```

## Expected Endpoints

The tests expect the following endpoints to be available:

### API Endpoints
- `GET /health` - Health check
- `GET /api/echo` - Echo endpoint
- `GET /api/todos/{id}` - Get todo by ID
- `GET /api/todos` - Get all todos

### UI Endpoints  
- `GET /` - Home page
- `GET /todos` - Todo manager page

## Requirements

- Python 3.11+
- pytest
- httpx
- Docker (for running the application container)