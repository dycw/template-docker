from typing import Any

from beartype import beartype
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
@beartype
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@router.get("/items/{item_id}")
@beartype
def read_item(*, item_id: int, q: str | None = None) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@router.put("/items/{item_id}")
@beartype
def update_item(*, item_id: int, item: Item) -> dict[str, Any]:
    return {"item_name": item.name, "item_id": item_id}
