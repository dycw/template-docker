from beartype import beartype
from fastapi import FastAPI

from app import dummyroutes
from app import routes


@beartype
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(dummyroutes.router)
    app.include_router(routes.router)
    return app


app = create_app()
