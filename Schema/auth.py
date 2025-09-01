from pydantic import BaseModel, Field

class GoogleUserDataSchema(BaseModel):
    id : int
    email : str
    name : str
    google_access_token : str

class YandexUserDataSchema(BaseModel):
    id : int
    email : str = Field(alias="default_email")
    name : str = Field(alias="real_name")
    yandex_access_token : str
