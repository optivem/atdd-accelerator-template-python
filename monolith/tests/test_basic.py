"""
Basic smoke tests for the application.
These tests verify basic functionality is working.
"""

import pytest


@pytest.mark.smoke
def test_basic_python():
    """Test that Python is working"""
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_basic_imports():
    """Test that basic imports work"""
    try:
        import sys
        import os
        assert True
    except ImportError:
        assert False, "Basic Python imports failed"


@pytest.mark.smoke 
def test_project_structure():
    """Test that we can find our main module"""
    try:
        import src.main
        assert hasattr(src.main, 'app')
    except ImportError as e:
        assert False, f"Failed to import main module: {e}"