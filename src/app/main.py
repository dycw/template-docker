from beartype import beartype
from fastapi import FastAPI

from app.core.logging import configure_logging
from app.routes import dummy, users


@beartype
def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(dummy.router)
    app.include_router(users.router)
    app.on_event("startup")(configure_logging)()
    return app


app = create_app()
