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
    assert response.json() == "0"

def test_get_item_valid_mock(mocker):
    mocker.patch('api.get_database', return_value={'id': 1, 'description': '0'})
    response = client.get('/items/1')
    assert response.status_code == 200
    assert response.json() == "0"

def test_get_item_absent_id():
    response = client.get("/items/1000")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not in the database.'}

def test_get_item_absent_id_mock(mocker):
    mocker.patch('api.get_database', return_value={'detail': 'Item not in the database.'})
    response = client.get('/items/1000')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not in the database.'}

def test_get_item_string_id():
    response = client.get("/items/'1'")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'input': "'1'", 'loc': ['path', 'id'], 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'type': 'int_parsing'}]}

def test_create_item_valid():
    response = client.post("items", json={"id": 22, "description": "147"})
    assert response.status_code == 200
    assert response.json() == {"id": 22, "description": "147"}

def test_create_item_wrong_description():
    response = client.post("/items", json={"id": 23, "description": "146"})  # TODO: Isolate this test
    assert response.status_code == 400
    assert response.json() == {'detail': 'Wrong description.'}

def test_create_item_wrong_id():
    response = client.post("/items", json={"id": 22, "description": "140"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Wrong id.'}
