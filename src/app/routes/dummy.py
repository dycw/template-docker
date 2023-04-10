from typing import Any

from beartype import beartype
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/")
@beartype
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@router.get("/items/{item_id}")
@beartype
async def read_item(*, item_id: int, q: str | None = None) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@router.put("/items/{item_id}")
@beartype
async def update_item(*, item_id: int, item: Item) -> dict[str, Any]:
    return {"item_name": item.name, "item_id": item_id}


@router.get("/ping")
@beartype
async def pong(*, settings: Settings = Depends(get_settings)) -> dict[str, str | bool]:
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
