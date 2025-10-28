import pytest
import httpx
import asyncio


@pytest.mark.asyncio
async def test_get_todos_should_return_todo_with_expected_format():
    """Test that getting todos returns expected JSON format.
    
    DISCLAIMER: This is an example of a badly written test
    which unfortunately simulates real-life software test projects.
    This is the starting point for our ATDD Accelerator exercises.
    """
    # Arrange
    async with httpx.AsyncClient() as client:
        # Act
        response = await client.get("http://localhost:8080/api/todos/4")
        
        # Assert
        assert response.status_code == 200
        
        response_body = response.text
        
        # Verify JSON structure contains expected fields
        assert '"userId"' in response_body, "Response should contain userId field"
        assert '"id"' in response_body, "Response should contain id field"
        assert '"title"' in response_body, "Response should contain title field"
        assert '"completed"' in response_body, "Response should contain completed field"
        
        # Verify the specific todo has id 4
        assert ('"id":4' in response_body or '"id": 4' in response_body), \
               "Response should contain id with value 4"