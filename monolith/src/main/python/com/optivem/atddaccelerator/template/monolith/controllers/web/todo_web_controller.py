from fastapi import APIRouter
from fastapi.responses import FileResponse


todo_web_router = APIRouter()


@todo_web_router.get("/todos")
async def todos():
    """Serve the todos page."""
    return FileResponse("src/main/resources/static/todos.html")