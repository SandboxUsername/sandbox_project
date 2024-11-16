from fastapi.testclient import TestClient
from api import app

client = TestClient(app=app)

def test_healthy_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Working': True}

def test_healthy_check_mulfunctioning():
    response = client.get("/wrong-url")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

def test_get_item_valid():
    response = client.get("/items/1")
    response.status_code == 200
    response.json() == 4

def test_get_item_invalid():
    response = client.get("/items/1000")
    response.status_code == 404
    response.json() == {'detail': 'Item not in the database.'}

