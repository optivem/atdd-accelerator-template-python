import pytest
from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to ATDD Accelerator Template"}


def test_app_title():
    """Test that the app has the correct title"""
    assert app.title == "ATDD Accelerator Template"
    assert app.version == "0.1.0"