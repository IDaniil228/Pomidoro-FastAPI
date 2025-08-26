from pydantic import BaseModel

class GoogleUserDataSchema(BaseModel):
    id : int
    email : str
    name : str
    google_access_token : str
