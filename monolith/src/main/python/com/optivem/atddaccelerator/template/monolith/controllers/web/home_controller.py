from fastapi import APIRouter
from fastapi.responses import FileResponse


home_router = APIRouter()


@home_router.get("/")
async def home():
    """Serve the home page."""
    return FileResponse("src/main/resources/static/index.html")