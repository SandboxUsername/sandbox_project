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
    assert response.status_code == 200
    assert response.json() == 0

def test_get_item_absent_id():
    response = client.get("/items/1000")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not in the database.'}

def test_get_item_string_id():
    response = client.get("/items/'1'")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'input': "'1'", 'loc': ['path', 'id'], 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'type': 'int_parsing'}]}
