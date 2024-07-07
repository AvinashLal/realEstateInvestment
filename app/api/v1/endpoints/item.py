from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud, models, schemas
from app.utils.deps import get_db

router = APIRouter()

# In-memory storage for items
items = [1,2,3]

@router.get("/items/", response_model=List[int])
def read_items(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated_item
    return updated_item

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    item = items.pop(item_id)
    return item
