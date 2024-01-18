from pydantic import EmailStr

# class CreateUser(BaseModel):
#     name: str
#     password: str
#
#     @validator("password", pre=True)
#     def hash_password(cls, password: str) -> str:
#         return get_password_hash(password)


from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    role: int
    password: str
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    role: int
    password: str
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    # id: int
    # email: EmailStr
    # is_active: bool = True
    # is_superuser: bool = False
    # is_verified: bool = False

