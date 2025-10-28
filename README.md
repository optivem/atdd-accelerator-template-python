# ATDD Accelerator Template (Python)

[![commit-stage-monolith](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/commit-stage-monolith.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/commit-stage-monolith.yml)
[![acceptance-stage](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/acceptance-stage.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/acceptance-stage.yml)
[![qa-stage](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-stage.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-stage.yml)
[![qa-signoff](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-signoff.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/qa-signoff.yml)
[![prod-stage](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/prod-stage.yml/badge.svg)](https://github.com/optivem/atdd-accelerator-template-python/actions/workflows/prod-stage.yml)

This is a Python implementation of the ATDD (Acceptance Test-Driven Development) Accelerator Template, migrated from the original Java version. It provides a complete web application with API endpoints and UI for managing todos, built using FastAPI and modern Python practices.

## Technology Stack

- **Python 3.11+**: Modern Python with type hints
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server implementation
- **Pydantic**: Data validation using Python type annotations
- **Pytest**: Testing framework with async support
- **HTTPX**: Modern HTTP client for Python
- **Docker**: Containerization

## Project Structure

```
monolith/
├── src/
│   ├── main/
│   │   ├── python/
│   │   │   └── com/optivem/atddaccelerator/template/monolith/
│   │   │       ├── models/          # Data models (Pydantic)
│   │   │       ├── controllers/     # Request handlers
│   │   │       │   ├── api/         # API endpoints
│   │   │       │   └── web/         # Web page controllers
│   │   │       ├── config.py        # Application configuration
│   │   │       └── monolith_application.py  # Main FastAPI app
│   │   └── resources/
│   │       └── static/              # Static HTML files
│   └── test/
│       └── python/                  # Unit tests
├── requirements.txt                 # Python dependencies
├── pyproject.toml                  # Project configuration
└── Dockerfile                     # Container definition

system-test/
└── src/test/python/                # System and E2E tests
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/optivem/atdd-accelerator-template-python.git
   cd atdd-accelerator-template-python
   ```

2. **Set up virtual environment**
   ```bash
   cd monolith
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python -m uvicorn com.optivem.atddaccelerator.template.monolith.monolith_application:app --host 0.0.0.0 --port 8080 --reload
   ```

5. **Access the application**
   - Web UI: http://localhost:8080
   - API Documentation: http://localhost:8080/docs
   - Todo Manager: http://localhost:8080/todos

### Running with Docker

1. **Build the Docker image**
   ```bash
   cd monolith
   docker build -t atdd-accelerator-template-python .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 atdd-accelerator-template-python
   ```

### Running Tests

1. **Unit tests**
   ```bash
   cd monolith
   pytest src/test/python/
   ```

2. **System tests** (requires running application)
   ```bash
   cd system-test
   pip install -r requirements.txt
   pytest src/test/python/
   ```

## API Endpoints

- `GET /api/echo` - Simple echo endpoint
- `GET /api/todos/{id}` - Fetch todo by ID from external API
- `GET /` - Home page
- `GET /todos` - Todo manager page

## Configuration

The application can be configured using environment variables:

- `TODOS_API_HOST`: External todos API host (default: https://jsonplaceholder.typicode.com)
- `PORT`: Server port (default: 8080)
- `HOST`: Server host (default: 0.0.0.0)

## Migration from Java

This project has been migrated from the original Java Spring Boot implementation to Python FastAPI. Key changes include:

- **Java Spring Boot** → **Python FastAPI**
- **Gradle** → **pip + pyproject.toml**
- **JUnit** → **pytest**
- **Jackson/JSON** → **Pydantic models**
- **RestTemplate** → **HTTPX async client**
- **application.yml** → **Pydantic Settings with environment variables**

The core functionality and API contract remain the same to ensure compatibility with existing clients and tests.

## License

[![Unlicense](https://img.shields.io/badge/license-Unlicense-lightgrey.svg)](http://unlicense.org/)

This project is released under [The Unlicense](http://unlicense.org) — a public domain dedication.

## Contributors

- [Valentina Jemuović](https://github.com/valentinajemuovic)
- [Jelena Cupać](https://github.com/jcupac)
