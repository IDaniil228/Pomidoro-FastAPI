from pydantic import BaseModel

class UserLoginSchema(BaseModel):
    user_id : int
    access_token: str

    class Config:
        from_attributes = True

    def __str__(self):
        return f"id - {self.user_id}  токен - {self.access_token}"