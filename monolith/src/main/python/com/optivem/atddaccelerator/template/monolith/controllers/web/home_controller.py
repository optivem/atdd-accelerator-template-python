from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path


home_router = APIRouter()


@home_router.get("/")
async def home():
    """Serve the home page."""
    # Get the static files directory path relative to this file
    current_dir = Path(__file__).parent
    static_dir = current_dir.parent.parent.parent.parent.parent.parent.parent / "main" / "resources" / "static"
    index_file = static_dir / "index.html"
    
    if index_file.exists():
        return FileResponse(str(index_file))
    else:
        return {"message": "Welcome to ATDD Accelerator Template - Python!"}