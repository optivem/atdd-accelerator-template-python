from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
import os
from pathlib import Path

from .config import settings
from .controllers.api.todo_api_controller import todo_api_router
from .controllers.api.echo_api_controller import echo_api_router
from .controllers.web.home_controller import home_router
from .controllers.web.todo_web_controller import todo_web_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        description="ATDD Accelerator Template - Monolith (Python)"
    )
    
    # Get the static files directory path relative to this file
    current_dir = Path(__file__).parent
    static_dir = current_dir.parent.parent.parent.parent.parent / "main" / "resources" / "static"
    
    # Mount static files if the directory exists
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
    
    # Include API routers
    app.include_router(todo_api_router, prefix="/api")
    app.include_router(echo_api_router, prefix="/api")
    
    # Include web routers
    app.include_router(home_router)
    app.include_router(todo_web_router)
    
    return app


# Create the app instance
app = create_app()


def main():
    """Main entry point for the application."""
    uvicorn.run(
        "com.optivem.atddaccelerator.template.monolith.monolith_application:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )


if __name__ == "__main__":
    main()