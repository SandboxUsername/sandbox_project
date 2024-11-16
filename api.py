from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {'Working': True}

items = {str(x + 1): x * 7 for x in range(21)}

@app.get("/items/{id}")
def get_item(id):
    item = items[id]
    return item