import pytest
from fastapi.testclient import TestClient

# We'll need to adjust this import path based on the actual structure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'main', 'python'))

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
    # The response should be HTML content
    assert "text/html" in response.headers.get("content-type", "")


def test_todos_page(client):
    """Test the todos page endpoint.""" 
    response = client.get("/todos")
    assert response.status_code == 200
    # The response should be HTML content
    assert "text/html" in response.headers.get("content-type", "")