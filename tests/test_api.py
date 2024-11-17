from fastapi.testclient import TestClient
from api import app, get_database
import pytest
from database_management import Item

client = TestClient(app=app)

def mock_get_database():
    return [Item(id=1, description='First item'), Item(id=2, description='Second item')]

@pytest.fixture
def override_db_dependency():
    app.dependency_overrides[get_database] = mock_get_database
    yield
    app.dependency_overrides.clear()

def test_healthy_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Working': True}

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [Item(id=1, description='First item'), Item(id=2, description='Second item')]