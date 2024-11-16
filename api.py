from fastapi import FastAPI, HTTPException
from schemas import Item

app = FastAPI()

@app.get("/")
def health_check():
    return {'Working': True}

items = {x + 1: str(x * 7) for x in range(21)}

@app.get("/items/{id}")
def get_item(id: int):
    if id not in items:
        raise HTTPException(status_code=404, detail='Item not in the database.')
    item = items[id]
    return item

@app.post("/items")
def create_item(item: Item):
    if item.id - 1 != int(item.description) / 7:
        raise HTTPException(status_code=400, detail="Wrong description.")
    items[item.id] = item.description
    return item
