from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.schemas.base import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
