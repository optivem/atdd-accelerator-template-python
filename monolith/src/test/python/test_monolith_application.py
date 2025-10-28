import pytest
import sys
import os
from pathlib import Path

# Add the main Python source to the path
main_python_path = Path(__file__).parent.parent.parent / "main" / "python"
sys.path.insert(0, str(main_python_path))

from fastapi.testclient import TestClient
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