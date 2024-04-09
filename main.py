from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    id: int = 23
    id: int = 23
    id: int = 23

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World TOur"}


@app.get("/items/{item_id}")
def read_item(item_id: int, user: Union[str, None] = None):
    return {"item_id": item_id, "user": user}

@app.post("/info")
def take_data(item: Item):
    return item