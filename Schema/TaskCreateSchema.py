from pydantic import BaseModel

class TaskCreateSchema(BaseModel):
    title : str

    class Config:
        from_attributes = True