from os import environ

from beartype import beartype
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.routes import dummy, users


@beartype
def reg_tor(app: FastAPI, /) -> None:
    register_tortoise(
        app,
        db_url=environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


@beartype
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(dummy.router)
    app.include_router(users.router)
    reg_tor(app)
    return app


app = create_app()
