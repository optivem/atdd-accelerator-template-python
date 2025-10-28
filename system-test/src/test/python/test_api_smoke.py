import pytest
import httpx


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_api_smoke_test():
    """Basic smoke test for API endpoints."""
    async with httpx.AsyncClient() as client:
        # Test echo endpoint
        echo_response = await client.get("http://localhost:8080/api/echo")
        assert echo_response.status_code == 200
        assert echo_response.text == '"Echo"'  # JSON string response
        
        # Test todos endpoint (using a known good todo ID)
        todos_response = await client.get("http://localhost:8080/api/todos/1")
        assert todos_response.status_code == 200
        
        # Basic validation that it's a valid JSON with expected structure
        todo_data = todos_response.json()
        assert "userId" in todo_data
        assert "id" in todo_data
        assert "title" in todo_data
        assert "completed" in todo_data