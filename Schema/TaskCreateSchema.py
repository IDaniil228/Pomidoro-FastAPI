from pydantic import BaseModel

class TaskCreateSchema(BaseModel):
    id : int
    title : str
    user_id : int

    class Config:
        from_attributes = True