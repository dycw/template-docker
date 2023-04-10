from sqlalchemy import Column, Integer, String

from app.db.schemas.base import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    email = Column(String)
    password = Column(String)
