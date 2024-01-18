from fastapi_users import FastAPIUsers

from auth.cooki import auth_backend
from database import User
from auth.manager import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
