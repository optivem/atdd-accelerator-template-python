from fastapi import APIRouter, HTTPException, Depends
import httpx
from typing import Annotated

from ...models.todo import Todo
from ...config import settings


todo_api_router = APIRouter()


async def get_http_client() -> httpx.AsyncClient:
    """Dependency to provide HTTP client."""
    return httpx.AsyncClient()


@todo_api_router.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(
    todo_id: int,
    http_client: Annotated[httpx.AsyncClient, Depends(get_http_client)]
) -> Todo:
    """Get a todo by ID from external API."""
    url = f"{settings.todos_api_host}/todos/{todo_id}"
    
    try:
        async with http_client as client:
            response = await client.get(url)
            response.raise_for_status()
            todo_data = response.json()
            return Todo(**todo_data)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"External API error: {e}")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Request error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")