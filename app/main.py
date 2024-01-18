from fastapi import FastAPI

from auth.cooki import auth_backend
from routers.auth import fastapi_users
from routers.game import game
from routers.singin import check
from schemes.user import UserCreate, UserRead


def init_router(application: FastAPI):
    application.include_router(game, prefix="/game")
    application.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth",tags=["auth"], ),
    application.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"], )
    application.include_router(check)


def make_app() -> FastAPI:
    _app = FastAPI(
        title="Bulls and Cows",
        description="The game for logic",
        version="0.1"
    )
    init_router(_app)
    return _app


app = make_app()
