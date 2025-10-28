import pytest
from fastapi.testclient import TestClient

# Direct import since we'll install as editable package
from com.optivem.atddaccelerator.template.monolith.monolith_application import create_app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    app = create_app()
    return TestClient(app)


def test_echo_endpoint(client):
    """Test the echo API endpoint."""
    response = client.get("/api/echo")
    assert response.status_code == 200
    assert response.json() == "Echo"


def test_home_page(client):
    """Test the home page endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    # Should return JSON fallback if static files don't exist
    assert response.status_code == 200


def test_todos_page(client):
    """Test the todos page endpoint.""" 
    response = client.get("/todos")
    assert response.status_code == 200
    # Should return JSON fallback if static files don't exist  
    assert response.status_code == 200