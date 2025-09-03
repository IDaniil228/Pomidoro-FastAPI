from pydantic import BaseModel

class TaskSchema(BaseModel):
    id : int
    title : str
    user_id : int

    class Config:
        from_attributes = True