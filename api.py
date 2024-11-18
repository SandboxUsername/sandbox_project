from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from database_management import Item, get_database

app = FastAPI()

@app.get("/")
def healthy_check():
    return {'Working': True}

@app.get("/items")
def get_items(session: Session = Depends(get_database)):
    return session.exec(select(Item)).all()

@app.post("/item")
def create_item(item: Item, session: Session = Depends(get_database)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
