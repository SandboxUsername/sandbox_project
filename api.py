from fastapi import Depends, FastAPI, HTTPException
from schemas import Item

app = FastAPI()

@app.get("/")
def health_check():
    return {'Working': True}

DDBB = {x + 1: str(x * 7) for x in range(21)}

def get_database():
    return DDBB

@app.get("/items/{id}")
def get_item(id: int, db=Depends(get_database)):
    if id not in db:
        raise HTTPException(status_code=404, detail='Item not in the database.')
    item = db[id]
    return item

@app.post("/items")
def create_item(item: Item, db=Depends(get_database)):
    if item.id - 1 != int(list(db.keys())[-1]):
        raise HTTPException(status_code=400, detail="Wrong id.")
    if item.id - 1 != int(item.description) / 7:
        raise HTTPException(status_code=400, detail="Wrong description.")
    # breakpoint()
    db[item.id] = item.description
    # breakpoint()
    return item
