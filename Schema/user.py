from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    username : str | None = None
    password: str | None = None
    email : str | None = None
    name : str | None = None
    google_access_token : str | None  = None
    yandex_access_token : str | None  = None

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    user_id : int
    access_token: str

    class Config:
        from_attributes = True

    def __str__(self):
        return f"id - {self.user_id}  токен - {self.access_token}"