from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path


todo_web_router = APIRouter()


@todo_web_router.get("/todos")
async def todos():
    """Serve the todos page."""
    # Get the static files directory path relative to this file
    current_dir = Path(__file__).parent
    static_dir = current_dir.parent.parent.parent.parent.parent.parent.parent / "main" / "resources" / "static"
    todos_file = static_dir / "todos.html"
    
    if todos_file.exists():
        return FileResponse(str(todos_file))
    else:
        return {"message": "Todo Manager - Python Implementation"}