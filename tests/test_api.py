from fastapi.testclient import TestClient
from api import app

client = TestClient(app=app)

def test_healthy_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Working': True}