from fastapi.testclient import TestClient
from api import app, get_database
import pytest
from database_management import Item
from unittest.mock import MagicMock

client = TestClient(app=app)

@pytest.fixture
def mock_session():
    mock_session = MagicMock()
    mock_session.exec.return_value.all.return_value = [
        {"id": 0, "description": "First element"},
        {"id": 1, "description": "Second element"},
    ]
    return mock_session

@pytest.fixture
def override_db_dependency(mock_session):
    app.dependency_overrides[get_database] = lambda: mock_session
    yield
    app.dependency_overrides.clear()

def test_healthy_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Working': True}

def test_get_items(override_db_dependency):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
                {"id": 0, "description": "First element"},
                {"id": 1, "description": "Second element"},
            ]