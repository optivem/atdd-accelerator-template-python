"""
Walking skeleton for ATDD Accelerator Template.
Minimal FastAPI application to get started with ATDD.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
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


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to ATDD Accelerator Template"}


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