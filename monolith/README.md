# Monolith Application

This is a walking skeleton FastAPI application that serves as the foundation for ATDD development.

## Technology Stack

- **Python 3.11+**: Modern Python with type hints
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server implementation
- **Pydantic**: Data validation using Python type annotations
- **Pytest**: Testing framework with async support
- **Docker**: Containerization

## Quick Start

1. **Set up virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python -m uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload
   ```

4. **Access the application:**
   - Home: http://localhost:8080
   - Health Check: http://localhost:8080/health
   - API Docs: http://localhost:8080/docs
   - Todo Manager: http://localhost:8080/todos

## Project Structure

```
src/
├── main.py              # Main FastAPI application
└── static/              # Static HTML files
tests/
├── test_main.py         # Unit tests
└── test_basic.py        # Basic smoke tests
requirements.txt         # Python dependencies
pyproject.toml          # Project configuration
Dockerfile              # Container definition
```

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /` - Home page (HTML)
- `GET /todos` - Todo manager page (HTML)
- `GET /api/echo` - Simple echo endpoint
- `GET /api/todos/{id}` - Get todo by ID
- `GET /api/todos` - Get all todos

## Development

### Running Tests
```bash
# All tests
pytest

# Smoke tests only
pytest -m smoke

# With verbose output
pytest -v
```

### Building Docker Image
```bash
docker build -t atdd-accelerator-template-python .
```

### Running with Docker
```bash
docker run -p 8080:8080 atdd-accelerator-template-python
```

## ATDD Development

This is a walking skeleton designed for ATDD development. To add features:

1. Write a failing acceptance test
2. Write minimal code to make it pass
3. Refactor if needed
4. Repeat

Follow the TODO comments in `src/main.py` to add your features using the ATDD approach.
