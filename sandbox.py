from typing import List
from sqlmodel import Field, SQLModel, Session, create_engine, select

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    description: str

DATABASE_URL = 'sqlite:///./first_database.db'
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)


def insert_item(item: Item) -> Item:
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

def get_items() -> List[Item]:
    with Session(engine) as session:
        return session.exec(select(Item)).all()

insert_item(Item(description='First item'))
items = get_items()
print(items)