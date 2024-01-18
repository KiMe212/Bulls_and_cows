from fastapi import Depends, APIRouter

from database import User
from routers.auth import fastapi_users

current_user = fastapi_users.current_user()

check = APIRouter()


@check.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"

# import uuid
#
# from fastapi import FastAPI
# from fastapi_users import FastAPIUsers
#
# from .db import User
# from .schemas import UserRead, UserUpdate
#
# fastapi_users = FastAPIUsers[User, uuid.UUID](
#     get_user_manager,
#     [auth_backend],
# )
#
# app = FastAPI()
# app.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )
