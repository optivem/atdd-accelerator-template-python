import pytest
import httpx


@pytest.mark.asyncio
async def test_ui_smoke_test():
    """Basic smoke test for UI endpoints."""
    async with httpx.AsyncClient() as client:
        # Test home page
        home_response = await client.get("http://localhost:8080/")
        assert home_response.status_code == 200
        assert "text/html" in home_response.headers.get("content-type", "")
        
        # Test todos page
        todos_response = await client.get("http://localhost:8080/todos")
        assert todos_response.status_code == 200
        assert "text/html" in todos_response.headers.get("content-type", "")