from typing import Any

from beartype import beartype
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.db.engines import yield_sess
from app.db.schemas.users import UserDB
from app.models import UserInM, UserOutM

router = APIRouter(prefix="/users")


@router.post("/create", response_model=UserOutM, status_code=HTTP_201_CREATED)
@beartype
def create(*, user: UserInM, sess: Session = Depends(yield_sess)) -> Any:
    sess.add(user_db := UserDB(email=user.email, password=user.password))
    sess.commit()
    return user_db


@router.get("/")
@beartype
def root(*, sess: Session = Depends(yield_sess)) -> list[Any]:
    return sess.query(UserDB).all()
