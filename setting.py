from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    db_name: str = "C:\Python\FastAPI\db.sqlite"