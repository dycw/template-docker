from beartype._decor.main import beartype
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.db.engines import yield_sess
from app.db.schemas.users import UserDB
from app.models import UserInM
from app.models import UserOutM


router = APIRouter(prefix="/users")


@router.post("/create", response_model=UserOutM, status_code=HTTP_201_CREATED)
@beartype
def create(*, user: UserInM, sess: Session = Depends(yield_sess)) -> UserDB:
    sess.add(user := UserDB(email=user.email, password=user.password))
    sess.commit()
    return user


@router.get("/")
@beartype
def root(*, sess: Session = Depends(yield_sess)) -> list[UserDB]:
    return sess.query(UserDB).all()
