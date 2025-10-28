import pytest
import httpx


@pytest.mark.asyncio  
async def test_ui_e2e_test():
    """End-to-end test for UI functionality."""
    async with httpx.AsyncClient() as client:
        # Test that home page contains expected content
        home_response = await client.get("http://localhost:8080/")
        assert home_response.status_code == 200
        home_content = home_response.text
        assert "Hello World!" in home_content
        assert "ATDD Accelerator Template - Python" in home_content
        assert 'href="/todos"' in home_content
        
        # Test that todos page contains expected content
        todos_response = await client.get("http://localhost:8080/todos")
        assert todos_response.status_code == 200
        todos_content = todos_response.text
        assert "Todo Fetcher" in todos_content
        assert 'id="fetchTodo"' in todos_content
        assert '/api/todos/' in todos_content