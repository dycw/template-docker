from beartype import beartype
from fastapi import FastAPI

from app import dummyroutes
from app import routes
from app.core.logging import configure_logging


@beartype
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(dummyroutes.router)
    app.include_router(routes.router)
    app.on_event("startup")(configure_logging)()
    return app


app = create_app()
