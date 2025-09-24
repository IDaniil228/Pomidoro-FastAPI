from pydantic import BaseModel

class EmailMessage(BaseModel):
    text: str
    subject: str
    to_mail: str