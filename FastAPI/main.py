from fastapi import FastAPI, HTTPException as HTTPEx
from pydantic import BaseModel

app = FastAPI()

items = []
class Item(BaseModel):
    item:str

@app.get("/")
def root():
    return {"Hello":"World"}

@app.post("/items")
def create_items(item:Item):
    items.append(item.item)
    return items

@app.get("/items/{item_id}")
def get_items(item_id: int) -> str:
    if item_id >= len(items):
        raise HTTPEx(status_code=404, detail="Item not found")
    return items[item_id]