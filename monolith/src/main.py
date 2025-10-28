"""
Walking skeleton for ATDD Accelerator Template.
Minimal FastAPI application to get started with ATDD.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(
    title="ATDD Accelerator Template",
    description="ATDD Walking Skeleton",
    version="0.1.0",
)

# Mount static files
static_path = Path(__file__).parent / "static"
if static_path.exists():
    app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/", response_class=HTMLResponse)
async def home():
    """Home page with HTML response"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ATDD Accelerator Template - Python</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>Welcome to ATDD Accelerator Template - Python</p>
        <a href="/todos">View Todos</a>
    </body>
    </html>
    """


@app.get("/todos", response_class=HTMLResponse)
async def todos_page():
    """Todos page with HTML response"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Todo Fetcher</title>
    </head>
    <body>
        <h1>Todo Fetcher</h1>
        <button id="fetchTodo">Fetch Todo</button>
        <div id="todoResult"></div>
        <script>
            document.getElementById('fetchTodo').addEventListener('click', async () => {
                const response = await fetch('/api/todos/1');
                const todo = await response.json();
                document.getElementById('todoResult').innerHTML = JSON.stringify(todo);
            });
        </script>
    </body>
    </html>
    """


@app.get("/api/echo")
async def echo():
    """Echo endpoint for health checks and testing"""
    return "Echo"  # Return string that becomes JSON string "Echo"


@app.get("/api/todos/{todo_id}")
async def get_todo(todo_id: int):
    """Get a specific todo by ID"""
    # Mock response for testing
    return {
        "userId": 1,
        "id": todo_id,
        "title": f"Sample todo {todo_id}",
        "completed": False
    }


@app.get("/api/todos")
async def get_todos():
    """Get all todos"""
    return [
        {"userId": 1, "id": 1, "title": "Sample todo 1", "completed": False},
        {"userId": 1, "id": 2, "title": "Sample todo 2", "completed": True},
    ]


# TODO: Add your features here following ATDD approach:
# 1. Write a failing acceptance test
# 2. Write minimal code to make it pass
# 3. Refactor if needed
# 4. Repeat

# Example first feature:
# @app.get("/todos")
# async def get_todos():
#     """Get all todos"""
#     return []