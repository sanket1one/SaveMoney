from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/")
async def read_items():
    return [{"id": 1, "name": "Expense 1"}, {"id": 2, "name": "Expense 2"}]

@router.post("/")
async def create_item(item: dict):
    return {"id": 3, "name": item.get("name")}
