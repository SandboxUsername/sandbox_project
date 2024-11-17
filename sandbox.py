from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()
client = TestClient(app=app)

DDBB = {x + 1: str(x * 7) for x in range(21)}

def get_database():
    return DDBB

@app.get("/items/{id}")
def get_item(id: int, db=Depends(get_database)):
    if id not in db:
        raise HTTPException(status_code=404, detail='Item not in the database.')
    item = db[id]
    return item

def mock_get_database():
    return {1: '2'}

def test_get_item_valid_mock():
    app.dependency_overrides[get_database] = mock_get_database
    print(app.dependency_overrides)
    response = client.get('/items/1')
    assert response.status_code == 200
    assert response.json() == "2"
