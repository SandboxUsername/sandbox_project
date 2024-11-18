from sqlmodel import Field, SQLModel, Session, create_engine

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    description: str

DATABASE_URL = 'sqlite:///./api_database.db'
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_database():
    with Session(engine) as session:
        yield session

