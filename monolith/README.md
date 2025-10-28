# Monolith Application (Python)

This is the main Python FastAPI application for the ATDD Accelerator Template.

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
   python -m uvicorn com.optivem.atddaccelerator.template.monolith.monolith_application:app --host 0.0.0.0 --port 8080 --reload
   ```

   Or use the provided scripts:
   ```bash
   # Windows
   start.bat
   
   # Linux/macOS
   ./start.sh
   ```

4. **Access the application:**
   - Home: http://localhost:8080
   - API Docs: http://localhost:8080/docs
   - Todo Manager: http://localhost:8080/todos

## Project Structure

```
src/
├── main/
│   ├── python/              # Python source code
│   │   └── com/optivem/atddaccelerator/template/monolith/
│   │       ├── models/      # Data models
│   │       ├── controllers/ # API and web controllers
│   │       ├── config.py    # Configuration
│   │       └── monolith_application.py  # Main app
│   └── resources/
│       └── static/          # Static HTML/CSS/JS files
└── test/
    └── python/              # Unit tests
```

## API Endpoints

- `GET /api/echo` - Echo endpoint
- `GET /api/todos/{id}` - Get todo by ID
- `GET /` - Home page
- `GET /todos` - Todo manager page

## Environment Variables

- `TODOS_API_HOST` - External API host (default: https://jsonplaceholder.typicode.com)
- `HOST` - Server host (default: 0.0.0.0)
- `PORT` - Server port (default: 8080)
- `DEBUG` - Debug mode (default: false)

## Development

### Running Tests
```bash
pytest src/test/python/
```

### Building Docker Image
```bash
docker build -t atdd-accelerator-template-python .
```

### Running with Docker
```bash
docker run -p 8080:8080 atdd-accelerator-template-python
```
