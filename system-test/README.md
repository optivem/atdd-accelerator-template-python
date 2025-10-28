# System Test (Python)

This directory contains system tests for the Python application using pytest.

## Instructions

1. **Navigate to the system-test directory:**
   ```bash
   cd system-test
   ```

2. **Install test dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Docker Containers:**
   ```bash
   docker compose up -d
   ```

4. **Run All Tests:**
   ```bash
   pytest src/test/python/
   ```

5. **Run Smoke Tests Only:**
   ```bash
   pytest src/test/python/ -m smoke
   ```

6. **Run E2E Tests Only:**
   ```bash
   pytest src/test/python/ -m e2e
   ```

7. **Run with verbose output:**
   ```bash
   pytest src/test/python/ -v
   ```

8. **Stop Docker Containers:**
   ```bash
   docker compose down
   ```

## Test Structure

```
src/test/python/
├── test_api_e2e.py      # API end-to-end tests
├── test_api_smoke.py    # API smoke tests
├── test_ui_e2e.py       # UI end-to-end tests
└── test_ui_smoke.py     # UI smoke tests
```

## Requirements

- Python 3.9+
- pytest
- httpx
- Docker (for running the application container)