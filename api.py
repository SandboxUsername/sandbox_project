from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def health_check():
    return {'Working': True}

items = {str(x + 1): x * 7 for x in range(21)}

@app.get("/items/{id}")
def get_item(id):
    if id not in items:
        raise HTTPException(status_code=404, detail='Item not in the database.')
    item = items[id]
    return item